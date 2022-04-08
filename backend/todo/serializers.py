
# todo/serializers.py

from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # id: token or id number, title: product, description: category, completed: status run
        fields = ('id', 'title', 'description', 'completed')
