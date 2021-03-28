from django.shortcuts import render
from .models import Activity
# Create your views here.


def manage_entities(request):
    activities = Activity.objects.all()
    return render(request, 'activity/manage_entities.html', {'activities': activities})
