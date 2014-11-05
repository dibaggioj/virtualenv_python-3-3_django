from django.contrib import admin
from polls.models import Choice, Question

# Register your models here.

# admin.site.register(Question) # Django constructs a default form representation. To display the Polls app on the admin index page, need to tell the admin that Question objects have an admin interface
# admin.site.register(Choice)
class ChoiceInLine(admin.TabularInline): # displays "Choice text" and "Votes" fields next to each other for each question choice (compared to .StackedInline)
	model = Choice # Choice objects are edited on the Question admin page
	extra = 3 # By default, provide enough fields for 3 choices

class QuestionAdmin(admin.ModelAdmin): # 1. Create a model admin object
	#fields = ['pub_date', 'question_text'] # this just flips the pub_date and question_text fields from their default order
	fieldsets = [
		(None,					{'fields': ['question_text']}), # first element of each tuple in fieldsets is the title of the fieldset
		('Date information', 	{'fields': ['pub_date'], 'classes':['collapse']}), # "collapse" class idplays a particular fieldset initial collapsed
	]
	inlines = [ChoiceInLine] # links to Choice model, so that you can add/edit/delete choice_text and vote field entries from the Questions page
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date'] # adds a "Filter" sidebar that lets you filter the change list by the pub_date field. The type of filter displayed depends on the type of field you are filtering on. pub_date is a DateTimeField, so Django knows to give appropriate filter options: "Any date," "Today," "Past 7 days," "This month," "This year."
	search_fields = ('question_text', 'pub_date') # adds a search box at the top of the change lists. When someone enters search terms, Django will search only the question_text and pub_date fields.


admin.site.register(Question, QuestionAdmin) # 2. Pass in the new model admin object as the second argument, in order to change the admin options for the object

