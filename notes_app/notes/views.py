from django.shortcuts import render,redirect
from .models import Notes
from .forms import NoteForm

# Create your views here.


def list(request):
    all_notes=Notes.objects.all()
    return render(request,'notes/notesList.html',{'notes': all_notes})

def detail(request,pk):
    note=Notes.objects.get(pk=pk)
    return render(request,'notes/noteDetail.html',{'note':note})

def create(request):
    form=NoteForm()
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes.list')
            
    return render(request,'notes/newNote.html',{'form':form})

def edit(request,pk):
    note=Notes.objects.get(pk=pk)
    form=NoteForm(instance=note)
    if request.method=='POST':
        form=NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes.list')
        
    context={'form':form ,'note':note}
    return render(request,'notes/noteEdit.html',context)

