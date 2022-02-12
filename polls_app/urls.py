from unicodedata import name
from django.urls import path
from . import views

app_name = "polls_app"


urlpatterns = [
    # /polls/
    path(route="", view=views.IndexView.as_view(), name="index"),
    path("specific/<int:pk>/", view=views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", view=views.ResultsView.as_view(), name="results"),
    path("<int:pk>/vote/", view=views.vote, name="vote"),
]
