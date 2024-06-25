from django.urls import path

from api.post.views import (
    PostListCreateView,
    PostRetriveView,
    PostMeListView,
    PostMeRetrieveUpdateDestoryView,
)

from api.comment.views import  CommentListView


urlpatterns = [
    path("", PostListCreateView.as_view()),
    path("me/", PostMeListView.as_view()),
    path("<uuid:uuid>/", PostRetriveView.as_view(lookup_field="uuid")),
    path("<int:pk>/", PostRetriveView.as_view()),
    path("me/<int:pk>/", PostMeRetrieveUpdateDestoryView.as_view()),
    path(
        "me/<uuid:uuid>/", PostMeRetrieveUpdateDestoryView.as_view(lookup_field="uuid")
    ),
    path("<uuid:uuid>/comment/", CommentListView.as_view()),
    path("<int:pk>/comment/", CommentListView.as_view()),
]
