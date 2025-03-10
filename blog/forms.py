from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    The CommentForm class inherits from the forms.ModelForm class.
    This class is used to create a form for the Comment model.
    The CommentForm class has the following attributes:
    '''
    class Meta:
        model = Comment
        fields = ('body',)