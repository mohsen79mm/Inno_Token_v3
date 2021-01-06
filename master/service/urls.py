from django.urls import path


from .views import categorylist,subcategorylist,servicelist,userlist,services
urlpatterns = [

    path('show_cats/',categorylist.as_view(),name='category_list'),
    path('show_subs/<int:cat_id>',subcategorylist.as_view(), name='subcategory_list'),
    path('show_services/<int:sub_id>',servicelist.as_view(), name='service_list'),
    path('show_users/<int:service_id>',userlist.as_view(), name='user_list'),
    path('services/',services.as_view(), name='services'),





]