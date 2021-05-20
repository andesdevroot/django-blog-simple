from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:              # clase para validar data desde el formulario
        model = Comment
        fields = ('name', 'email','body')

