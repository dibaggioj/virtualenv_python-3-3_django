from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
#from django.template import RequestContext, loader

from polls.models import Choice, Question

# Create your views here.

#Using two generic views: ListView and DetailView, to “display a list of objects” and “display a detail page for a particular type of object” respectively

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice']) # request.POST['choice'] returns the ID of the selected choice, as a string (note: request.POST values are always strings). Unlike request.GET (which also accesses GET data in the same way), request.POST alters data via a POST call
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': p,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,))) # Redirect to results page. Unlike HttpResponse, HttpResponseRedirect takes a single argument: the URL to which the user will be redirected (see the following point for how we construct the URL in this case). Using the reverse() function helps avoid hacing to hardcode a URL in the view function; it is given the name of the view we want to pass control to and the variable portion of the URL pattern that points to the view Original: return HttpResponse("You're voting on question %s." % question_id)
		# Always return an HttpResponseRedirect after successfully dealing with Post data. This prevents data from being posted twice if a user his the Back button

