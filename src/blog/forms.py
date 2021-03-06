from django import forms
from .models import Comment


class NewCommentForm(forms.ModelForm):

    class Meta:

        # fields
        model = Comment
        fields = ("content",)
        labels = {
            'content': ('Commentaire'),
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Ecrivez un commentaire',})
        }