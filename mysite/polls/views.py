from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic
#from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from polls.models import Choice, Question
from polls.forms import QuestionForm

# Create your views here.

# Using two generic views: ListView and DetailView, to display a list of objects and display a detail page for a
# particular type of object respectively


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions.
        """
        return Question.objects.filter( # returns a queryset containing Questions whose pub_date is less than or equal
            # to - that is, earlier than or equal to - timezone.now
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet"""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet"""
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice']) # request.POST['choice'] returns the ID of the
        # selected choice, as a string (note: request.POST values are always strings). Unlike request.GET (which also
        # accesses GET data in the same way), request.POST alters data via a POST call
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,))) # Redirect to results page.
            # Unlike HttpResponse, HttpResponseRedirect takes a single argument: the URL to which the user will be
            # redirected (see the following point for how we construct the URL in this case). Using the reverse()
            # function helps avoid hacing to hardcode a URL in the view function; it is given the name of the view we
            # want to pass control to and the variable portion of the URL pattern that points to the view Original:
            # return HttpResponse("You're voting on question %s." % question_id)
            # Always return an HttpResponseRedirect after successfully dealing with Post data. This prevents data from
            # being posted twice if a user his the Back button


def get_question(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            question_body = request.POST.get('your_question', '')
            new_question = Question(question_text=question_body, pub_date=timezone.now())
            new_question.save()

            characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
                          'x','y','z']
            for i in range(0, 5):
                answer_text = 'your_answer_' + characters[i]
                new_answer = request.POST.get(answer_text, '')
                if new_answer != '':
                    new_choice = Choice(question=new_question, choice_text=new_answer, votes=0)
                    new_choice.save()
            # process the data in form.cleansed_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/polls/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, 'polls/question.html', {'form': form})






