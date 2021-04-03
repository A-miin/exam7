from django.urls import path

from .views import (
    IndexPollView,
    ViewPollView,
    CreatePollView,
    UpdatePollView,
    DeletePollView,

)

urlpatterns=[
    path('',IndexPollView.as_view() , name = 'poll-list'),
    path('poll/<int:pk>', ViewPollView.as_view(), name = "poll-view"),
    path('poll/new', CreatePollView.as_view(), name = "poll-create"),
    path('poll/<int:pk>/edit', UpdatePollView.as_view(), name='poll-update'),
    path('poll/<int:pk>/delete', DeletePollView.as_view(), name='poll-delete')

]