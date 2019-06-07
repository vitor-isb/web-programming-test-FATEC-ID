from django.urls import path
from . import views

urlpatterns = [
    path('', views.professor_list, name='professor_list'),
    path('faculdade/novoprofessor',views.new_teacher, name='new_teacher'),
    path('faculdade/formsucess',views.form_sucess,name='form_sucess'),
]