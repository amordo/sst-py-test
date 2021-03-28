from django.shortcuts import render

# Create your views here.


def manage_entities(request):
    return render(request, 'activity/manage_entities.html', {})
