from django.urls import path
from maths.views import math, add, sub, mul, div, maths_list, math_details, results_list, search

app_name="maths"
urlpatterns = [
    path('', math),
    path("add/<a>/<b>", add),
    path("sub/<a>/<b>", sub),
    path("mul/<a>/<b>", mul),
    path("div/<a>/<b>", div),
    path('histories/', maths_list, name='list'),
    path('histories/<int:id>', math_details, name='details'),
    path('results/', results_list, name='results'),
    path('search/', search, name='search'),

]
