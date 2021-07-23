from django.urls import path
from . import views



app_name ='books'


urlpatterns = [
        path('', views.allBooks,name='allbooks'),
        path('add',views.newBook,name='newbook'),
        path('<str:slug>/likes', views.like_dislike,name='like'),
        path('<str:slug>', views.singleBook,name='singlebook'),
        
]