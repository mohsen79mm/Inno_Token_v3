from django.urls import path
from .views import categorylist,subcategorylist,servicelist_cat,servicelist_sub,services , service_detail , search
urlpatterns = [

    path('show_cats/',categorylist.as_view(),name='category_list'),
    # path('show_subs/<int:cat_id>',subcategorylist.as_view(), name='subcategory_list'),
    path('show_subs/<int:cat_id>',subcategorylist, name='subcategory_list'),

    path('show_services_sub/<int:sub_id>',servicelist_sub.as_view(), name='service_sub'),
    path('show_services_cat/<int:cat_id>',servicelist_cat.as_view(), name='service_cat'),

    path('service_detail/<int:pk>',service_detail.as_view(), name='service_detail'),

    path('services/',services.as_view(), name='services'), #All Services Without Any Filter

    path('search/', search , name ='search') ,

]