from django.urls import path,include
from .views import PostList,postDetail,tagged,viewfront

urlpatterns = [
    path('' , PostList.as_view() , name='Blog'),
    
    path('tag/<str:tag>/' , tagged , name = 'tagged'),
    path('<str:url>/' , postDetail, name='post_detail'),
    
]
