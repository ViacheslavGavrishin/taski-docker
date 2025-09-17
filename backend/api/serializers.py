"""Docstring content"""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Docstring content"""

    class Meta:
        """Docstring content"""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
