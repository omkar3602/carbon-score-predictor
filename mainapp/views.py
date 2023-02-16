from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('adminuser')
        return render(request, 'mainapp/home.html')
    return render(request, 'mainapp/index.html')

def oxygen_emission(request):
    return render(request, 'mainapp/get_oxygen_emission.html')

def carbon_footprint(request):
    return render(request, 'mainapp/get_carbon_footprint.html')