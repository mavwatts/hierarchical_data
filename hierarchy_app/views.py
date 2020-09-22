from django.shortcuts import render
from hierarchy_app.models import Pokemon

# Create your views here.
def index_view(request):
    return render(request, 'index.html', {'pokemon': Pokemon.objects.all()})
