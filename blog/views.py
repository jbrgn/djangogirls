from django.shortcuts import render
from django.utils import timezone
from .models import Thing

# Create your views here.

def thing_list(request):
    things = Thing.objects.order_by('-created_date')
    return render(request, 'blog/thing_list.html', {'things': things})
