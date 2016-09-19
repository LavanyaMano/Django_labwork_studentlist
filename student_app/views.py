from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import StudentDetail

def index(request):
    details = StudentDetail.objects.all()
    context = {
    "details":details
    }
    return render(request,"student_app/index.html",context)

def detail(request,id):
    detail =get_object_or_404(StudentDetail,pk=id,published__lt=timezone.now())

    context = {
    "detail": detail
    }

    return render(request,"student_app/detail.html",context)