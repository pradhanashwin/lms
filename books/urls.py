from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.index, name='index'),
     # Individual URL
     path('add_new_individual/', views.add_new_individual,
          name='new_individual'),
     path('add_new_author/', views.add_new_author,
          name='new_author'),
     path('search_individual/', views.search_individual, name='search_individual'),
     path('show_individuals/', views.show_individuals,
          name='show_individuals_record'),
     path('delete/individual/<str:roll>/', views.delete_individual,
          name="delete_individual_data"),
     # Books URL
     path('view_books/', views.view_books, name='show_books'),
     path('view_book_record/<int:id>', views.view_book_record, name='view_book_record'),
     path('search_books/', views.search_books, name='search_books'),
     path('edit/book/<int:id>/', views.edit_book_data,
          name="edit_book_data"),
     path('delete/book/<int:id>/', views.delete_book, name="delete_book_data"),
     path('return_book/<int:id>/', views.return_issued_book,
          name="return_issued_book"),
     path('view_books_issued/', views.view_bissue, name='show_issue_record'),
     path('add_new_book/', views.add_new_book, name='add_new_book'),
     path('edit_issued/<int:id>/', views.edit_issued, name="edit_issued"),
     path('add_book_issue/', views.add_book_issue, name='book_issue'),
     path('add_new_book_instance/', views.add_new_book_instance,
          name='add_new_book_instance'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
