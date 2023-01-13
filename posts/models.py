from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        "posts.Author",
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )

    def __str__(self):
        return f"id:{self.id}, title:{self.title}"

class Author(models.Model):
    nick = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    biogram = models.TextField(null = True, blank = True)

    def __str__(self):
        return f"id:{self.id}, nick:{self.nick}"
