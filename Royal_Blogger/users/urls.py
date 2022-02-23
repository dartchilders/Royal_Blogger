from django.urls import path
from .views import ShowProfile, UserEditProfile, UserRegister, ChangePassword, EditProfilePage, Like

app_name = 'users'
urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('editprofile/', UserEditProfile.as_view(), name='editprofile'),
    path('password/', ChangePassword.as_view(template_name='registration/changepassword.html')),
    path('<int:pk>/edit_profile_page/', EditProfilePage.as_view(), name='editprofilepage'),
    path('<int:pk>/profile/', ShowProfile.as_view(), name='userprofilepage'),
    path('like/<int:pk>', Like, name='likepost'),
]