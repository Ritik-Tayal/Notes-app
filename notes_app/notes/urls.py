from django.urls import path
from . import views

urlpatterns = [
    path('notes/',views.list,name='notes.list'),
    path('notes/<int:pk>/',views.detail,name='notes.detail'),
    path('notes/new/',views.create,name='notes.new'),
    path('notes/edit/<int:pk>/',views.edit,name='notes.edit'),
    path('notes/delete/<int:pk>/',views.deleteNote,name='notes.delete'),
]
