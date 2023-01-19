from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm

def posts_list(request):
    """wyswietla liste wszystkich postow """
    if request.method == "POST":
        form = PostForm(data=request.POST)

        if form.is_valid():
            author = Author.objects.get(pk=int(form.cleaned_data['author']))
            data = form.cleaned_data.copy()
            data['author'] = author
            Post.objects.create(**data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy wpis"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Błąd! Nie udało sie utworzyć nowego wpisu"
            )

    form = PostForm()
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/p_list.html",
        context={"posts":posts, "form":form}
    )

def post_details(request, id):
    """wyswietla szczegoly pojedynczego postu"""
    post = Post.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/p_details.html",
        context={"post":post}
    )


def authors_list(request):
    """wyswietla liste wszystkich autorow"""
    if request.method == "POST":
        form = AuthorForm(data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(**data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Nowy użytkownik utworzony"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Błąd! Spróbuj jeszcze raz."
            )

    form = AuthorForm()
    authors = Author.objects.all()
    return render(
        request=request, 
        template_name = "posts/a_list.html",
        context={"authors":authors, "form":form}
    )


def author_details(request, id):
    """wyswietla info o autorze"""
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/a_details.html",
        context={"author":author}

    )