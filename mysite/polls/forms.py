from django import forms


class QuestionForm(forms.Form):
    your_question = forms.CharField(label='Add a new question', max_length=250)
    your_answers = {
        'a': forms.CharField(label="A", max_length=100, min_length=1),
        'b': forms.CharField(label="B", max_length=100, min_length=1, required=False),
        'c': forms.CharField(label="C", max_length=100, min_length=1, required=False),
        'd': forms.CharField(label="D", max_length=100, min_length=1, required=False),
        'e': forms.CharField(label="E", max_length=100, min_length=1, required=False),
    }
