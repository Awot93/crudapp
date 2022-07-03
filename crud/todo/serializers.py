from rest_framework import serializers
from .models import TodoApp


class TodoAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoApp
        fields = '__all__'