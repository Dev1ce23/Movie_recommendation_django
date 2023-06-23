from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .recommendation import movie_details, single_movie



from .forms import ReviewForm
# Create your views here.
def starting_page(request):
    return render(request,"authentication/index.html")

def signup(request):

    
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("login")
            
            
        return render(request, 'authentication/signup.html', {"form": form})

    else:
        form = UserCreationForm()
        print(form.fields)
    return render(request,'authentication/signup.html', {
       "form": form
    })

def loginView(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'authentication/signup.html', {'error': "Invalid username/password"})

        
    return render(request,'authentication/signup.html')


@login_required(login_url='login')
def home(request):
     return render(request,'authentication/home.html')

def movieSearch(request):
    if request.method == 'GET':
        movie_search = request.GET.get('search')
        json_data = movie_details(movie_search)
        print(json_data)
        return JsonResponse(json_data)
    
def movie(request,slug):
    if request.method == 'GET':
        json_data = single_movie(slug)
        print(json_data)
        return render(request,'authentication/movie.html',{'data':json_data})       

def logoutPage(request):
    logout(request)
    return redirect('login')