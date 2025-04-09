
from django.urls import path
from . import views

#localhost:8000/app
urlpatterns = [
    
    path('', views.all_app, name ='all_app'),
    path('<int:app_id>/', views.app_details, name ='app_details'),
    path('app_stores/', views.app_store_view, name ='app_stores'),
]
