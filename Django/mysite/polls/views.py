from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Question
from django.template import loader, TemplateDoesNotExist
from django.views import generic
from django.utils import timezone



class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_context_data(self):
    #     print('hello')
    #     return self.abc

    def get_queryset(self):
        print('hello')
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
            


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    # context_object_name = 'data'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

    # def get_object(self, queryset=None):
    #     obj = Question.objects.get(pk=self.kwargs['pk'])
    #     print('hello123')
    #     return obj



    def get_context_data(self, **kwargs):
        print('hello')
        context = {}
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        # b = context
        # a = super().get_context_data(**context)
        context.setdefault('view', self)
        print(context)
        return context


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
