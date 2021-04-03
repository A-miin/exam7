from django.urls import path

from .views import (
    IndexPollView,
    ViewPollView,
)

urlpatterns=[
    path('',IndexPollView.as_view() , name = 'poll-list'),
    path('poll/<int:pk>', ViewPollView.as_view(), name = "poll-view")

]