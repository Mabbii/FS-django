"""imports"""
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """ItemForm Model"""
    class Meta:
        """Getting data/fields from model"""
        model = Item
        fields = ['name', 'done']
