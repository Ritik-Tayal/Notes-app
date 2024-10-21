from django.shortcuts import render,redirect
from .models import Notes
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def list(request):
    all_notes=Notes.objects.filter(user=request.user)
    return render(request,'notes/notesList.html',{'notes': all_notes})

@login_required(login_url='login')
def detail(request,pk):
    note=Notes.objects.get(pk=pk)
    return render(request,'notes/noteDetail.html',{'note':note})

@login_required(login_url='login')
def create(request):
    form=NoteForm()
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            note=form.save(commit=False)
            note.user=request.user
            note.save()
            form.save()
            return redirect('notes.list')
            
    return render(request,'notes/newNote.html',{'form':form})

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteNote(request,pk):
    note=Notes.objects.get(pk=pk)
    if request.method=='POST':
        note.delete()
        return redirect('notes.list')
    return render(request,'notes/noteDelete.html')