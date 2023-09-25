from django.contrib import messages, auth
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import CustomerRegistrationForm
from .models import Department, Course, Form
from django.contrib.auth.models import User
# Create your views here.


def allCourdep(request,c_slug=None):
    c_page=None
    courses_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Department,slug=c_slug)
        courses_list=Course.objects.all().filter(department=c_page,available=True)
    else:
        courses_list=Course.objects.all().filter(available=True)
    paginator=Paginator(courses_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        courses=paginator.page(page)
    except (EmptyPage,InvalidPage):
        courses=paginator.page(paginator.num_pages)

    return render(request,"department.html",{'department':c_page,'courses':courses})


class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render (request,'register.html',locals())
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successfull')
        else:
            messages.warning(request,'Invalid')
        return render(request, 'register.html', locals())

# def profileView(request):
#     return render('request','button.html')

def new_page(request):
    # Your view logic here
    return render(request, 'button.html')
# def form(request):
#     return render(request, 'form.html')

def form(request):
    if request.method=='POST':
        form=Form(request.POST)
        name=request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        email = request.POST['email']
        phone=request.POST['phone']
        address = request.POST['address']
        course = request.POST['course']
        department = request.POST['department']
        purpose = request.POST['purpose']
        material = request.POST.get('material')
        age = request.POST['age']
        form=Form(name=name,dob=dob,gender=gender,email=email,phone=phone,address=address,course=course,department=department,purpose=purpose,material=material,age=age)
        form.save()
        return render(request, 'confirm.html')

    return render(request, 'form.html')


def confirm(request):
    return render(request, 'confirm.html')