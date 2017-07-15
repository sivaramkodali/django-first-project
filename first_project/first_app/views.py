from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import topic,webpage,accessrecord,db_users
from first_app.forms import CreateUser

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def first_page(request):
    my_dict = {"insert_me":"I am first project"}
    return render(request,'first_app/first_page.html',my_dict)

def second_page(request):
    webpages_list = accessrecord.objects.order_by('date')
    date_dict = {'access_record':webpages_list}
    return render(request,'first_app/second_page.html',context=date_dict)

def users_page(request):
    users_list = db_users.objects.order_by('firstname')
    users_dict = {'users_list':users_list}
    return render(request,'first_app/users_page.html',context=users_dict)

from . import forms


def forms_page(request):
    form = forms.FormPage()
    if request.method == 'POST':
        form = forms.FormPage(request.POST)

        if form.is_valid():
            print("Validation Success!")
            print("NAME :"+ form.cleaned_data['name'])
            print("EMAIL :"+ form.cleaned_data['email'])
            print("TEXT :"+ form.cleaned_data['text'])

    return render(request,'first_app/forms_page.html',{'form':form})

def create_users(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users_page(request)
    return render(request,'first_app/create_users.html',{'form':form})


def relative_page(request):
    return render(request,'first_app/relative_page.html')

from first_app.forms import UserForm, UserProfileInfoForm

def register_page(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form =UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'first_app/registration.html',{'user_form':user_form,
                                                         'profile_form':profile_form,
                                                         'registered':registered})

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse('Invalid login details supplied.')
    else:
        return render(request,'first_app/login_page.html',{})
