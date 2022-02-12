from unicodedata import name
from django.urls import path
from . import views

app_name = "polls_app"


urlpatterns = [
    # /polls/
    path(route="", view=views.index, name="index"),
    # /polls/5/detail/
    path("specific/<int:question_id>/", view=views.detail, name="detail"),
    # /polls/5/results/
    path("<int:question_id>/results/", view=views.results, name="results"),
    # /polls/5/vote/
    path("<int:question_id>/vote/", view=views.vote, name="vote"),
]
