from django.shortcuts import render

# Create your views here.
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.template import loader
# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Post
from .models import Question, Choice

from django.shortcuts import get_object_or_404, render


def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("practice2.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def html(request):
    return render(request, 'practice.html')


def show_name(request):
    context = {'name_list': Post.objects.all()}
    print(context)
    return render(request, 'practice.html', context=context)


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

#
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "detail.html", {"question": question})


class IndexView(generic.ListView):
    template_name = "practice2.html"
    context_object_name = "latest_question_list"
    model = Question
    ordering = ['-pub_date']
    print(context_object_name)


    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())




class DetailView(generic.DetailView):
    model = Question
    template_name = "detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "results.html"

