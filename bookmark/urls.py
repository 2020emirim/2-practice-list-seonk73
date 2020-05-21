from django.urls import path

from bookmark.views import BookmarkList, BookmarkCreateView

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkList.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
]
