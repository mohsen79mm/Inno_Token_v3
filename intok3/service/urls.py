from django.urls import path

from .views import show_categories,show_sub,show_service,show_user_service

urlpatterns = [

    # path('show_services/', get_services,name='services'),
    # path('service_detail/<int:serv_id>',service_detail,name='service-detail'),
    path('',show_categories,name='show-categories'),
    path('show_subs/<int:cat_id>',show_sub,name='show-subs'),
    path('show_services/<int:subcategory_id>',show_service,name='show-services'),
    path('show_provider/<int:service_id>',show_user_service,name='show-provider'),

]