from django.urls import path

from .views import BookListView, BookDetail, BookCreate, BookDelete, BookUpdate, index_view, CreateReview

from . import views
urlpatterns = [
    path('', views.index_view, name='index'),
    path('book/', BookListView.as_view(), name='list-book'),
    path('detail/<int:pk>/', BookDetail.as_view(), name='detail-book'),
    path('create/', BookCreate.as_view(), name='create-book'),
    path('delete/<int:pk>/', BookDelete.as_view(), name='delete-book'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='update-book'),
    path('book/<int:book_id>/review/', CreateReview.as_view(), name='review'),
]
