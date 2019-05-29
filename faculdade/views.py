from django.shortcuts import render
from .models import Professor
# Create your views here.
def professor_list(request):
    professores = Professor.objects.all()
    return render(request, 'faculdade/professor_list.html', {'professores':professores})