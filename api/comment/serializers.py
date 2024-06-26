from rest_framework import serializers

from api.post.serializers import PostCommentSerializer
from content.models import Comment
from api.user.serializers import UserPublicSerializer
from api.post.querysets import PUBLIC_POSTS_QUERYSET


class CommentSerializer(serializers.ModelSerializer):

    owner = UserPublicSerializer(read_only=True)
    post = PostCommentSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            "id",
            "uuid",
            "post",
            "owner",
            "body",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "uuid",
            "post",
            "owner",
            "created_at",
        ]


class CommentCreateSerializer(serializers.Serializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.SlugRelatedField(
        slug_field="uuid", queryset=PUBLIC_POSTS_QUERYSET
    )
    body = serializers.CharField()
    # body = serializers.CharField(required = False)