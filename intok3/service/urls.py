from django.urls import path


from .views import categorylist,subcategorylist,servicelist
urlpatterns = [

    path('',categorylist.as_view(),name='category-list'),
    path('show_subs/<int:cat_id>',subcategorylist.as_view(), name='subcategory-list'),
    path('show_services/<int:sub_id>',servicelist.as_view(), name='service-list'),




]