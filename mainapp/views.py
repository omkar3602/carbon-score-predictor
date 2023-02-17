from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.decorator import login_required_message
from .models import Oxygen_Emission
from utils.ml_helpers import predictOxygenEmission

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
    if request.user.is_admin:
            return redirect('adminuser')
    if request.method=="POST":
        data=request.POST
        plant_species=data['plant_species']
        light_intensity = data['light_intensity']
        carbon_emission = data['carbon_emission']
        temperature = data['temperature']
        ans=predictOxygenEmission(plant_species=plant_species, light_intensity=light_intensity, carbon_emission=carbon_emission, temperature=temperature)
        print(f'Prediction= {ans}')
        oxygen_model=Oxygen_Emission(plant_species=plant_species, light_intensity=light_intensity, carbon_emission=carbon_emission, temperature=temperature, oxygen_emission=ans)
        oxygen_model.save()
        return redirect('oxygen_emission')
    return render(request, 'mainapp/get_oxygen_emission.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def carbon_footprint(request):
    if request.user.is_admin:
            return redirect('adminuser')
    return render(request, 'mainapp/get_carbon_footprint.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def homeappliances(request):
    if request.user.is_admin:
            return redirect('adminuser')
    return render(request, 'mainapp/home_appliances.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def vehicles(request):
    if request.user.is_admin:
            return redirect('adminuser')
    return render(request, 'mainapp/vehicles.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def waste(request):
    if request.user.is_admin:
            return redirect('adminuser')
    return render(request, 'mainapp/waste.html')