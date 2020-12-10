from django.urls import include, path
from .views import StartupList,ProviderList,AcceleratorList,StartupDetail,AcceleratorDetail,ProviderDetail
urlpatterns = [

    path('startup_list/',StartupList.as_view(),name='startup_list'),
    path('provider_list/',ProviderList.as_view(),name='provider_list'),
    path('accelerator_list/',AcceleratorList.as_view(),name='accelerator_list'),
    path('startup_detail/<int:pk>',StartupDetail.as_view(),name='startup_detail'),
    path('provider_detail/<int:pk>',ProviderDetail.as_view(), name='provider_detail'),
    path('accelerator_detail/<int:pk>',AcceleratorDetail.as_view(), name='accelerator_detail'),
    

]