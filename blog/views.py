from django.shortcuts import render
from django.utils import timezone
from .models import Thing
from datetime import date

# Create your views here.

def thing_list(request):
    things = Thing.objects.order_by('-created_date')
    return render(request, 'blog/thing_list.html', {'things': things})

def thing_detail(request, thing_id):
    thing = Thing.objects.get(id=thing_id)
    return render(request, 'blog/thing_detail.html', {'thing': thing})

def about(request):
    geburtstag = date(1991,11,28)
    alter = date.today() - geburtstag
    jahre = int(alter.days//365.25)
    return render(request, 'blog/about.html', {'jahre': jahre})
