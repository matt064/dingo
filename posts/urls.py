from django.urls import path
from posts.views import posts_list, post_details, author_details, authors_list

app_name = "posts"
urlpatterns = [
    path("posts_list/", posts_list, name="p_list"),
    path("post_list/<int:id>", post_details, name='p_details'),
    path("authors/", authors_list, name="authors"),
    path('authors/<int:id>', author_details, name='a_details')
]