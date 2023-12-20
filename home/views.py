from django.shortcuts import render
from blog.models import  Post
from .models import  Testimonial, Employee, Profile, Project, Job
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.http import JsonResponse

# Create your views here.

def index(request):
    events = Post.objects.all().filter(category='EVENT').order_by('-timestamp')[0:3]
    testimonial = Testimonial.objects.all()
    project = Project.objects.all()
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'project':project,
        'latest': latest,
        'testimonial':testimonial,
        
    }
    return render(request, 'index.html', context)

def about(request):
    employee = Employee.objects.all()
    profile=get_object_or_404(Profile) 
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
      'employee':employee,
       'profile':profile,
       'latest': latest,
    }
    return render(request,'profile.html', context)

def Team(request):
    employee = Employee.objects.all()
    context= {
      'employee':employee,

    }

    return render(request,'team.html',context)


def Product_impact(request):

    return render(request, 'impact.html')

def Recycle(request):


    return render(request, 'recycle.html')

def Print(request):

    return render(request, 'print.html')
    
def Job(request):

    return render(request, 'jobs.html')
def Donate(request):

    return render(request, 'donate.html')