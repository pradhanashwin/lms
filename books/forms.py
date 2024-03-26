from django import forms
from .models import Individual, Book, Book_Issue, BookInstance, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        
class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_title', 'author', 'book_pages', 'summary', 'image']


class Book_instanceForm(forms.ModelForm):
    class Meta:
        model=BookInstance
        exclude = ['id']


class Book_IssueForm(forms.ModelForm):
    class Meta:
        model=Book_Issue
        fields = '__all__'
        exclude = ['issue_date', 'due_date','remarks_on_return','date_returned']