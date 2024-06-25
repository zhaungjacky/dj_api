from django.urls import path
from api.comment.views import CommentCreateView, CommentRetrieveUpdateDestroyView,  CommentListView,CommentPostUUIDView
urlpatterns = [
    path("",CommentCreateView.as_view()),
    path("lists/",CommentListView.as_view()),
    path("<uuid:uuid>/",CommentRetrieveUpdateDestroyView.as_view(lookup_field="uuid")),
    path("post-uuid/<uuid:uuid>/",CommentPostUUIDView.as_view(lookup_field="uuid")),
]
