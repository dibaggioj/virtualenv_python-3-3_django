from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
#from django.template import RequestContext, loader
from polls.models import Choice, Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # Load the polls/index.html template, fill a context and return an HttpResponse object with the result of the rendered template.
	#return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object does not exist. There is also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get(). It raises Http404 if the list is empty.
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
	# return HttpResponse(response % question_id)

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

