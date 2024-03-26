from django.contrib import admin
from .models import Individual, Author, Book, BookInstance, Book_Issue

@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'address', 'Email')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'author', 'book_pages', 'summary')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'is_borrowed')

@admin.register(Book_Issue)
class BookIssueAdmin(admin.ModelAdmin):
    list_display = ('individual', 'book_instance', 'issue_date', 'due_date', 'date_returned', 'remarks_on_issue', 'remarks_on_return')
