from dataclasses import fields
from django import forms
from .models import TodoApp

class TodoAppForm(forms):
    class Meta:
        model = TodoApp
        fields = [
            "title",
            "description"
        ]