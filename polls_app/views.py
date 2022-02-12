from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls_app/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls_app/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse("You're looking at the result of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
