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

from .models import Poll, Choice
from .forms import PollForm, ChoiceForm

# Create your views here.


class IndexPollView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = ('-created_at')
    paginate_by = 5
    paginate_orphans = 1

class ViewPollView(DetailView):
    model = Poll
    template_name = 'poll/view.html'

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