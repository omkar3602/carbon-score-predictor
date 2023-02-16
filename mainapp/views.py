from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.decorator import login_required_message

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('adminuser')
        return render(request, 'mainapp/home.html')
    return render(request, 'mainapp/index.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def oxygen_emission(request):
    return render(request, 'mainapp/get_oxygen_emission.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def carbon_footprint(request):
    return render(request, 'mainapp/get_carbon_footprint.html')