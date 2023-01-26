from django import forms
from posts.models import Author, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "author")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'})
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"