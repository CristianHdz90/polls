from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    """
    This class allow creating Choices
    at the same time when a question is created.
    """

    model = Choice
    extra = 3  # Number of choices


class QuestionAdmin(admin.ModelAdmin):
    """
    Class to change how the Question
    object is shown in the Admin interface.
    """

    fields = ["pub_date", "question_text"]
    # Bind the choices to the questions
    inlines = [ChoiceInline]

    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text", "pub_date"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
