from django.shortcuts import render,redirect
from django.http import JsonResponse
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .recommendation import recommendations



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
        recommended_movies=recommendations(movie_search)
        api_key = 'c21718c5'  # Replace with your actual API key
        movie_data_dict = {}
    # Make a GET request to the OMDB API
        for movie_title in recommended_movies:
            url = f'http://www.omdbapi.com/?apikey={api_key}&t={movie_title}'
            response = requests.get(url)
            
            if response.status_code == 200:
                movie_data = response.json()
                movie_data_dict[movie_title] = movie_data
            else:
                return JsonResponse({'error': 'Failed to fetch movie data.'}, status=500)
            
        Json_response={
            'data':movie_data_dict
        }   
        return JsonResponse(Json_response)
    
    
    
def movie(request,slug):
    if request.method == 'GET':
        api_key = 'c21718c5'
        print(slug)
        url = f'http://www.omdbapi.com/?apikey={api_key}&t={slug}'
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
        return render(request,'authentication/movie.html',{'data':json_data})       

def logoutPage(request):
    logout(request)
    return redirect('login')