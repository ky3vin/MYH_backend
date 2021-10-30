from django.urls import path
from .views import adBoardList, adBoardDelete, adBoardDetail, adBoardUpdate, adBoardCreate, adBoardLike, adBoardFavorite, \
    adBoardLikeList, adBoardFavoriteList, adBoardMyList, adBoardApply, ApplyList, ApplyDetail


app_name = "adBoard"

urlpatterns = [
    path("", adBoardList.as_view(), name='index'),
    path("mylist/", adBoardMyList.as_view(), name='mylist'),
    path("create/", adBoardCreate.as_view(), name='create'),
    path("like/<int:photo_id>/", adBoardLike.as_view(), name='like'),
    path("favorite/<int:photo_id>/", adBoardFavorite.as_view(), name='favorite'),
    path("delete/<int:pk>/", adBoardDelete.as_view(), name='delete'),
    path("update/<int:pk>/", adBoardUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", adBoardDetail.as_view(), name='detail'),
    path("like/", adBoardLikeList.as_view(), name="like_list"),
    path("favorite/", adBoardFavoriteList.as_view(), name="favorite_list"),
    path("apply/<int:pk>/",adBoardApply.as_view(), name='apply'),
    path("apply_list/",ApplyList.as_view(), name='apply_list'),
    path("apply/detail/<int:pk>/", ApplyDetail.as_view(), name='apply_detail'),
]

from django.conf.urls.static import static

from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)