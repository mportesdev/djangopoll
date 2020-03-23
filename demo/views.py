from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'demo/index.html', context)


def detail(request, question_id):
    return render(request, 'demo/detail.html', {'question_id': question_id})


def results(request, question_id):
    return render(request, 'demo/results.html', {'question_id': question_id})


def vote(request, question_id):
    return render(request, 'demo/vote.html', {'question_id': question_id})
