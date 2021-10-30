from django.urls import path
from .views import PostList, PostDelete, PostDetail, PostUpdate, PostCreate, ClubList

app_name = "noticeBoard"
urlpatterns = [
    path("", PostList.as_view(), name='index'),
    #path("mylist/", PhotoMyList.as_view(), name='mylist'),
    path("create/", PostCreate.as_view(), name='create'),
    path("delete/<int:pk>/", PostDelete.as_view(), name='delete'),
    path("update/<int:pk>/", PostUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", PostDetail.as_view(), name='detail'),
    path("clublist/", ClubList.as_view(), name='clublist'),
    ]

from django.conf.urls.static import static

from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)