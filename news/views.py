from django.views.generic import ListView, DetailView

from .models import Event


class HomeView(ListView):
    model = Event
    ordering = ['date_of_event']
    template_name = 'index.html'


class EventView(ListView):
    model = Event
    ordering = ['date_of_event']
    template_name = 'events/event.html'
