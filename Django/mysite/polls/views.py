from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Question
from django.template import loader, TemplateDoesNotExist
from django.views import generic



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # abc = Question.objects.order_by('-pub_date')[:5]

    # def get_context_data(self):

    #     return self.abc

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'




# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]

#     try:
#         template = loader.get_template('polls/index.html')
#     except TemplateDoesNotExist:
#         raise Http404("Template path does not exist")

#     context = {
#             'latest_question_list': latest_question_list,
#         }
#     # return HttpResponse(template.render(context, request))
#     # return render(request, 'polls/index.html', context)

#     rp = HttpResponse(template.render(context, request))
#     # rp['Age'] = 120
#     return rp


# def detail(request, pk):
#     question = get_object_or_404(Question, pk=pk)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, pk):
#     question = get_object_or_404(Question, pk=pk)
#     return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)
