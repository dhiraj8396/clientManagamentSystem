from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Client
# Create your views here.
def AddNewClientView(request):
    client_objs =Client.objects.all()
    template_name = "ClientApp/add.html"
    context ={"client_objes":client_objs}
    return render(request, template_name, context)