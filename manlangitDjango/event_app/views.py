from django.shortcuts import render

def index(request):
    return render(request, 'event/index.html')

def upcoming_events(request):
    return render(request, 'event/upcoming_events.html')

def create_event(request):
    return render(request, 'event/create_event.html')
