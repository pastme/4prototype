from django.urls import path
from books.views import BookCreate, BookDelete, BookUpdate, BookDetailView

urlpatterns = [
    path('book/<slug:slug>-<int:id>/', BookDetailView.as_view(), name='book'),
    path('book/add/', BookCreate.as_view(), name='book-add'),
    path('book/update/<int:pk>/', BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
]
