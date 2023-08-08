from django.shortcuts import render, redirect
from App.models import EventOrganizer, Event
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# Home
def home(request):
    return render(request, 'intro.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})
# DATA EO
def data_eo(request):
    all_eventOrganizer = EventOrganizer.objects.all()
    return render(request, 'home.html', {"eos":all_eventOrganizer})
# ADD
def add_eo(request):
    if request.method == "POST":
        if request.POST.get('name') \
        and request.POST.get('address') \
        and request.POST.get('email') \
        and request.POST.get('telp') :
            eo = EventOrganizer()
            eo.name = request.POST.get('name')
            eo.address = request.POST.get('address')
            eo.email = request.POST.get('email')
            eo.telp = request.POST.get('telp')
            eo.save()
            return HttpResponseRedirect('/data_eo')
    else:
        return render(request, 'add.html')
# VIEW
def eo(request, eo_id):
    eo = EventOrganizer.objects.get(id = eo_id)
    if eo != None:
        return render(request, "edit.html", {'eo':eo})
# EDIT
def edit_eo(request):
    if request.method == "POST":
        eo = EventOrganizer.objects.get(id = request.POST.get('id'))
        if eo != None:
            eo.name = request.POST.get('name')
            eo.address = request.POST.get('address')
            eo.email = request.POST.get('email')
            eo.telp = request.POST.get('telp')
            eo.save()
            return HttpResponseRedirect('/data_eo')
# DELETE
def delete_eo(request, eo_id):
    eo = EventOrganizer.objects.get(id = eo_id)
    eo.delete()
    return HttpResponseRedirect('/data_eo')

def data_event(request):
    all_event = Event.objects.all()
    return render(request, 'homeEvent.html', {"events":all_event})

def add_event(request):
    eo_name = EventOrganizer.objects.all()
    if request.method == "POST":
        if request.POST.get('title') \
        and request.POST.get('description') \
        and request.POST.get('date') \
        and request.POST.get('organizer') :
            event = Event()
            event.title = request.POST.get('title')
            event.description = request.POST.get('description')
            event.date = request.POST.get('date')
            event.organizer = request.POST.get('organizer')
            event.save()
            return HttpResponseRedirect('/data_event')
    else:
        return render(request, 'addEvent.html', {"eoname":eo_name})

def event(request, event_id):
    event = Event.objects.get(id = event_id)
    if event != None:
        return render(request, "editEvent.html", {'event':event})
# EDIT
def edit_event(request):
    if request.method == "POST":
        event = Event.objects.get(id = request.POST.get('id'))
        if event != None:
            event.title = request.POST.get('title')
            event.description = request.POST.get('description')
            event.date = request.POST.get('date')
            event.organizer = request.POST.get('organizer')
            event.save()
            return HttpResponseRedirect('/edit_event')

def delete_event(request, event_id):
    event = Event.objects.get(id = event_id)
    event.delete()
    return HttpResponseRedirect('/data_event')

def informasi(request):
    return render(request, "informasi.html")