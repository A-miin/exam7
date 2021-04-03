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
# from .forms import IssueForm, SearchForm, ProjectForm

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
