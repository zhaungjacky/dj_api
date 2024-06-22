from django.urls import path

from api.post.views import PostListCreateView, PostRetriveUpdateDestoryView,PostMeListView

urlpatterns = [
    path("",PostListCreateView.as_view()),
    path("me/",PostMeListView.as_view()),
    path("<uuid:uuid>/",PostRetriveUpdateDestoryView.as_view(lookup_field="uuid")),
    path("<int:pk>/",PostRetriveUpdateDestoryView.as_view()),
]
