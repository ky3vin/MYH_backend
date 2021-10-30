# from django.urls import path, include
# from .views import HelloAPI, RegistrationAPI, LoginAPI, UserAPI#, ProfileUpdateAPI#, Activate
#
#
# urlpatterns = [
#     path("hello/", HelloAPI),
#     path("auth/register/", RegistrationAPI.as_view()),
#     path("auth/login/", LoginAPI.as_view()),
#     path("auth/user/", UserAPI.as_view()),
#     #path("profile/<int:id>/update/", ProfileUpdateAPI.as_view()),
#     #path('activate/<str:uidb64>/<str:token>', views.UserActive.as_view(), name='activate')
# ]


from django.urls import path
from . import views
from accounts.views import signup, login, logout, home, UserHome, PasswordResetView, PasswordResetConfirmView, member_modify
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    #path('profileUpdate/<int:pk>/', views.ProfileUpdateAPI.as_view(), name="profileupdate"),
    #path('profileupdate/<int:pk>/', views.user_profile.as_view(), name="profileupdate"),
    path('userHome/', UserHome, name='userHome'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #path('forgot_id/', views.ForgotIDView, name="forgot_id"),
    path('member_modify/', views.member_modify, name='member_modify'),
   ]






# from django.urls import path, include
# from .views import HelloAPI, RegistrationAPI, LoginAPI, UserAPI, ProfileUpdateAPI, Activate
# from . import views
#
#
#
# app_name = 'api'
#
# urlpatterns = [
#     path("hello/", HelloAPI),
#     path("auth/register/", RegistrationAPI.as_view()),
#     path("auth/login/", LoginAPI.as_view()),
#     path("auth/user/", UserAPI.as_view()),
#     path("auth/profile/<username>/update/", ProfileUpdateAPI.as_view()),
#     path('activate/<str:uidb64>/<str:token>', views.UserActive.as_view(), name='activate')
# ]


