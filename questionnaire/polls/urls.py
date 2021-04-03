from django.urls import path

from .views import (
    IndexPollView,
)

urlpatterns=[
    path('',IndexPollView.as_view() , name = 'poll-list'),

]