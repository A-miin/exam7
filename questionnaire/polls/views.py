from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.views.generic import (
    View,
    TemplateView,
    FormView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode

from .models import Poll, Choice, Answer
from .forms import PollForm, ChoiceForm, AnswerForm

# Create your views here.


class IndexPollView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = ('-created_at')
    paginate_by = 5
    paginate_orphans = 1

class ViewPollView(View):
    def get(self, request, *args, **kwargs):
        poll = Poll.objects.get(id=kwargs['pk'])
        form = ChoiceForm()
        return render(request,'poll/view.html',context={'poll':poll, 'form':form})

class CreatePollView(CreateView):
    template_name = 'poll/create.html'
    form_class = PollForm
    model = Poll
    success_url = reverse_lazy('poll-list')

class UpdatePollView(UpdateView):
    form_class = PollForm
    model = Poll
    template_name = 'poll/update.html'
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll-view', kwargs={'pk':self.kwargs.get('pk')})

class DeletePollView(DeleteView):
    model = Poll
    template_name = 'poll/delete.html'
    context_object_name = 'poll'
    success_url = reverse_lazy('poll-list')

class CreateChoiceView(CreateView):
    form_class = ChoiceForm
    model = Choice

    def get_success_url(self):
        return reverse('poll-view', kwargs={'pk':self.kwargs.get('pk')} )

    def form_valid(self, form):
        poll = get_object_or_404(Poll, id = self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)


class UpdateChoiceView(UpdateView):
    form_class = ChoiceForm
    model = Choice
    template_name = 'choice/update.html'
    context_object_name = 'choice'

    def get_success_url(self):
        choice = Choice.objects.get(id=self.kwargs.get('pk'))
        return reverse('poll-view', kwargs={'pk':choice.poll.id})

class DeleteChoiceView(DeleteView):
    model = Choice
    template_name = 'choice/delete.html'
    context_object_name = 'choice'

    def get_success_url(self):
        choice = Choice.objects.get(id=self.kwargs.get('pk'))
        return reverse('poll-view', kwargs={'pk': choice.poll.id})

class CreateAnswerView(CreateView):
    template_name = 'answer/create.html'
    form_class = AnswerForm
    model = Answer

    def get_success_url(self):
        return reverse('poll-view', kwargs={'pk':self.kwargs.get('pk')})

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        poll = Poll.objects.get(id=self.kwargs.get('pk'))
        return form_class(poll, **self.get_form_kwargs())

    def form_valid(self, form):
        poll = Poll.objects.get(id=self.kwargs.get('pk'))
        choice = form.cleaned_data.get('choice')
        answer=Answer(poll=poll, choice=choice)
        answer.save()
        return redirect('poll-list')






