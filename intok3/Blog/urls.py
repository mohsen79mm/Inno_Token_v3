from django.urls import path,include
from .views import PostList,postDetail,tagged

urlpatterns = [


    path('' , PostList.as_view() , name='Blog'),
    path('tag/<slug:tag>/' , tagged , name = 'tagged'),
    path('<str:url>/' , postDetail, name='post_detail'),
    
]