from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.all()
    

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def results(request, q_id):
    question = Question.objects.get(pk=q_id)
    context ={
        "question" : question
    }
    return render(request, "polls/results.html", context)


def vote(request, q_id):
    question = Question.objects.get(pk=q_id)
    choices =request.POST.getlist("choice")
    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes += 1
        choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(q_id, )))





def meme(request):
    return HttpResponse("<img src='https://www.meme-arsenal.com/memes/4a8e6d4124c75f8de55e002c067c430e.jpg'>")