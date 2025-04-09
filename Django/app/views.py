from django.shortcuts import render
from .models import AppVarity
from django.shortcuts import get_object_or_404
# Create your views here.
def all_app(request):
    apps = AppVarity.objects.all()
    return render(request,'app/all_app.html',{'apps':apps})

def app_details(request, app_id):
    app = get_object_or_404(AppVarity, pk = app_id)
    return render(request, 'app/app_details.html',{'app':app})

def app_store_view(request):
    return render(request, 'app/app_stores.html')