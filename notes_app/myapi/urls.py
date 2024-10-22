# myjsonapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.get_notes, name='get_notes'),
    path('create/',views.addNote),
    path('note<int:id>/',views.noteDetail),
]
