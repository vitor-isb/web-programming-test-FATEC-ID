from django.shortcuts import render
from .models import Professor
from .forms import ProfessorForm
# Create your views here.
def professor_list(request):
    professores = Professor.objects.all()
    return render(request, 'faculdade/professor_list.html', {'professores':professores})

def new_teacher(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"faculdade/salvo.html",{})
    else:      
        form = ProfessorForm()
        return render(request, 'faculdade/salvo.html', {'form':form})

def form_sucess(request):
    return render(request,'faculdade/salvo.html',{})