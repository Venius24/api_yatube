from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model

import datetime as dt

from posts.models import User, Post, Group, Comment

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = ['id', 'text', 'pub_date', 'author', 'image', 'group']
        read_only_fields = ['id', 'pub_date', 'author']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'title', 'slug', 'description']
        read_only_fields = ['id']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created']
        read_only_fields = ['id', 'author', 'post', 'created']
