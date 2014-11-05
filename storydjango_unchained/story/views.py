#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Line
from .decorators import Render

# Create your views here.

def home(request):
	#return HttpResponse("Hello world!") # no html
	return render_to_response("story/home.html", {'lines': Line.objects.all()})

@login_required
@Render("story/home.html")
def home(request):
	return {'lines': Line.objects.all()}
