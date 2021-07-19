from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Animal
# Create your views here.


def home(request):
    return render(request, 'home.html')

class AnimalDelete(DeleteView):
    model = Animal
    success_url = "/animals/"

class AnimalUpdate(UpdateView):
    model = Animal
    fields = "__all__"

class AnimalList(ListView):
    model = Animal

class AnimalCreate(CreateView):
    model = Animal
    fields = "__all__"
    success_url = "/animals/"

class AnimalDetail(DetailView):
    model = Animal

def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('animal_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
