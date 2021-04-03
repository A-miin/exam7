from django import forms

from .models import Poll, Choice, Answer

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question',)

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('option',)

class AnswerForm(forms.ModelForm):
    choice = forms.ModelChoiceField(queryset=None)

    def __init__(self, poll, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = poll.choices.all()

    class Meta:
        model=Answer
        fields=('choice',)



