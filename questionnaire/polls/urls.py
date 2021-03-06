from django.urls import path

from .views import (
    IndexPollView,
    ViewPollView,
    CreatePollView,
    UpdatePollView,
    DeletePollView,
    CreateChoiceView,
    UpdateChoiceView,
    DeleteChoiceView,
    CreateAnswerView,

)

urlpatterns=[
    path('',IndexPollView.as_view() , name = 'poll-list'),
    path('poll/<int:pk>', ViewPollView.as_view(), name =
    "poll-view"),
    path('poll/new', CreatePollView.as_view(), name = "poll-create"),
    path('poll/<int:pk>/edit', UpdatePollView.as_view(), name='poll-update'),
    path('poll/<int:pk>/delete', DeletePollView.as_view(), name='poll-delete'),
    path('poll/<int:pk>/choice/add>',CreateChoiceView.as_view(), name='choice-create'),
    path('poll/choice/<int:pk>/edit>', UpdateChoiceView.as_view(), name='choice-update'),
    path('poll/choice/<int:pk>/delete', DeleteChoiceView.as_view(), name='choice-delete'),
    path('answer/<int:pk>/create', CreateAnswerView.as_view(), name='answer-create' )
]