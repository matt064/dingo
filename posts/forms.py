from django import forms
from posts.models import Author


class PostForm(forms.Form):
    title = forms.CharField(required=True, max_length=255)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.ChoiceField(
        choices=((a.id, a.nick) for a in Author.objects.all())
    )

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = cleaned_data.get('author')

        if not (title or content or author):
            raise forms.ValidationError("Wszystkie wartości muszą być podane.")



class AuthorForm(forms.Form):
    nick = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254)
    biogram = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'nie wymagany'}),
        required=False,
        )

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        email = cleaned_data.get('email')
        biogram = cleaned_data.get('biogram')

        if not nick:
            raise forms.ValidationError("Błąd! Proszę podac nazwe użytkownika.")