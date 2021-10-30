from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('noticeBoard/', include('noticeBoard.urls')),
    path('', include('adBoard.urls')),
    path('accounts/',include('accounts.urls')),
]