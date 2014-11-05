from django.shortcuts import render

class Render(object):
	def __init__(self, template): # __inti__ to configure the decorator
		self.template = template # pass Render a template and store it on the object itself

	def __call__(self, function): # __call__ is called when the function is defined and returns the wrapper. This class makes callable objects, so when you call the object, by following the object with (), you pass in a function, it create wrapper, and then returns wrapper. This makes a configurable decorator here; whatever function gets decorated by this decorator is going to be replaced by wrapper
		self.function = function
		def wrapper(request, *args): # wrapper calls the original function (self.function)
			ctx = self.function(request, *args) # when calling the original function, *args (for catching any additional positional parameters) is passed in
			return render(request, self.template, ctx)
		return wrapper

