from django.shortcuts import render, redirect, HttpResponse
from .forms import IndividualForm, BookForm, Book_IssueForm, Book_instanceForm, AuthorForm
from .models import Individual, Book, Book_Issue, BookInstance, Author
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Count

def get_total_books_count():
    return Book.objects.count()

def get_available_books_count():
    return BookInstance.objects.filter(is_borrowed=False).count()

def get_issued_books_count():
    return BookInstance.objects.filter(is_borrowed=True).count()

def get_overdue_books_count():
    return Book_Issue.objects.filter(due_date__lt=datetime.now()).count()

def index(request):
    # Retrieve book-related data using reusable functions
    total_books = get_total_books_count()
    available_books = get_available_books_count()
    issued_books = get_issued_books_count()
    overdue_books = get_overdue_books_count()

    # Retrieve 10 most popular books
    popular_books = Book.objects.annotate(
        issue_count=Count('bookinstance__book_issue')
    ).order_by('-issue_count')[:10]

    # Retrieve 10 newly added books
    new_books = Book.objects.order_by('-id')[:10]

    # Pass all the data to the template
    context = {
        'total_books': total_books,
        'available_books': available_books,
        'issued_books': issued_books,
        'overdue_books': overdue_books,
        'popular_books': popular_books,
        'new_books': new_books,
    }

    return render(request, 'index.html', context)


def view_books(request):
    books = Book.objects.order_by('-id')
    context = {
        'books': books,
        'book_form': BookForm,
        'instance_form': Book_instanceForm
    }
    return render(request, 'view_books.html', context)


def view_book_record(request, id):
    book = get_object_or_404(Book, id=id)
    context = {
        'book': book,
        'book_form': BookForm,
        'instance_form': Book_instanceForm
    }
    return render(request, 'view_book_record.html', context)


def add_new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            book_instance = BookInstance(book=form)
            book_instance.save()
            return redirect('/view_books')
    else:
        context = {
                'book_form': BookForm,
                'instance_form': Book_instanceForm
            }
        return render(request, 'add_new_book.html', context)


def add_new_book_instance(request):
    if request.method == "POST":
        instance_form = Book_instanceForm(request.POST)
        if instance_form.is_valid():
            instance = instance_form.save(commit=False)
            # Set the book instance as not borrowed initially
            instance.is_borrowed = False
            instance.save()
            return redirect('/view_books')  # Redirect to the books view
    else:
        instance_form = Book_instanceForm()
        return render(request, 'add_new_book_instance.html', {'instance_form': instance_form})


def view_bissue(request):
    context = {
        "issue": Book_Issue.objects.order_by('-id'),
        "issueForm": Book_IssueForm,
        "book": BookInstance.objects.filter(is_borrowed=False)}
    return render(request, 'issue_records.html', context=context)

def add_book_issue(request):
    if request.method == "POST":
        issueForm = Book_IssueForm(request.POST)
        if issueForm.is_valid():
            # save data
            unsaved_form = issueForm.save(commit=False)
            book_to_save = BookInstance.objects.get(id=unsaved_form.book_instance.id)
            book_to_save.is_borrowed = True
            book_to_save.save()
            issueForm.save()
            issueForm.save_m2m()
        return redirect('/view_books_issued')
    else:
        context = {"issueForm": Book_IssueForm,
                   "book": BookInstance.objects.filter(is_borrowed=False)}
        return render(request, 'add_book_issue.html', context=context)

def add_new_individual(request):
    if request.method == "POST":
        individualForm = IndividualForm((request.POST))
        if individualForm.is_valid():
            individualForm.save()
            return redirect('/show_individuals')
    else:
        contex = {
            'individualForm': IndividualForm,
            'authorForm': AuthorForm
            }
    return (render(request, 'add_new_individual.html', context=contex))


def add_new_author(request):
    if request.method == "POST":
        authorForm = AuthorForm((request.POST))
        if authorForm.is_valid():
            authorForm.save()
            return redirect('/show_individuals')
    else:
        contex = {
            'individualForm': IndividualForm,
            'authorForm': AuthorForm
        }
    return (render(request, 'add_new_individual.html', context=contex))


def show_individuals(request):
    individuals = Individual.objects.order_by('-id')
    context = {
                'individuals': individuals,
                'individualForm': IndividualForm,
                'authorForm': AuthorForm
                }
    return render(request, 'show_individuals.html', context)


def search_books(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query'].lower()
        # Search books by title or author
        books_by_title = Book.objects.filter(book_title__icontains=query)
        authors = Author.objects.filter(name__icontains=query)
        books_by_author = Book.objects.filter(author__in=authors)

        # Combine the results
        books = (books_by_title | books_by_author).distinct()
        # Serialize the book data to JSON
        data = [{'id': book.id, 'book_title': book.book_title, 'author': book.author.name} for book in books]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse([], safe=False)


def search_individual(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query'].lower()
        individuals = Individual.objects.filter(fullname__icontains=query)
        # Serialize the individual data to JSON
        data = [{'fullname': individual.fullname, 'address': individual.address, 'Email': individual.Email} for individual in individuals]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse([], safe=False)
        
def edit_book_data(request, id):
    return HttpResponse(f"<label>A book with ID: {id} could not be edited...</label><h2>The feature is comming soon</h2>")

def delete_individual(request, roll):
    return HttpResponse(f"<h2>Delete individual</h2><label>individual with Roll Number: {roll} could not be deleted...</label><h2>The feature is comming soon</h2>")
    pass

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    # Check if any instance of the book is borrowed
    if book.bookinstance_set.filter(is_borrowed=True).exists():
        messages.error(request, "Cannot delete the book because it has borrowed instances.")
    else:
        # Check if the book has any instances
        if book.bookinstance_set.exists():
            # Book has instances, delete all instances first
            book.bookinstance_set.all().delete()
            messages.warning(request, "All instances of the book have been deleted.")
        
        # No instances or all instances deleted, delete the book
        book.delete()
        messages.success(request, "Book has been deleted successfully.")

    return redirect('show_books')

def return_issued_book(request, id):   
    # Retrieve the Book_Issue object
    book_issue = get_object_or_404(Book_Issue, id=id)
    
    # Update the date_returned field
    book_issue.date_returned = timezone.now()
    book_issue.save()
    
    # Update the is_borrowed field of the corresponding BookInstance
    book_instance = book_issue.book_instance
    book_instance.is_borrowed = False
    book_instance.save()
    
    # Redirect to the book_issued view
    return redirect('/view_books_issued')

def edit_issued(request, id):
    obj = Book_Issue.objects.get(id=id)
    return HttpResponse(f"<h2>Edit Issued Book</h2><label>Book <i>{obj.book_instance.book.book_title}</i> issued to <i>{obj.individual.fullname}</i> could not be edited..</label><h2>The feature is comming soon</h2>")