from django import forms


class QuestionForm(forms.Form):
    your_question = forms.CharField(label='Add a new question', max_length=250)