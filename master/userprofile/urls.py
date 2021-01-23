from django.urls import include, path
from .views import StartupList, ProviderList, AcceleratorList, StartupDetail, AcceleratorDetail, ProviderDetail, Login, SignUp, logout_view, SmsPassword, ChangePassword,User_profile , add_service,load_sub,CompleteProfile

urlpatterns = [
    path('startup_list/',StartupList.as_view(),name='startup_list'),
    path('provider_list/',ProviderList.as_view(),name='provider_list'),
    path('accelerator_list/',AcceleratorList.as_view(),name='accelerator_list'),
    path('startup_detail/<int:pk>',StartupDetail.as_view(),name='startup_detail'),
    path('provider_detail/<int:pk>',ProviderDetail.as_view(), name='provider_detail'),
    path('accelerator_detail/<int:pk>',AcceleratorDetail.as_view(), name='accelerator_detail'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    path('smspassword', SmsPassword.as_view(), name='smspass' ),
    path('changepassword', ChangePassword.as_view(), name='changepass' ),
    path('user_profile', User_profile, name='user_profile'),
    path('add_service',add_service.as_view(),name='add_service_client'),
    path('category_id',load_sub,name='category_id'),
    path('complete_profile', CompleteProfile.as_view(), name='complete_profile')

]