from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from utils.decorator import login_required_message
from .models import Oxygen_Emission, HomeAppliance_CO2_Emission, Vehicle_CO2_Emission
from utils.ml_helpers import predictOxygenEmission, predictHomeApplianceCarbonDioxide, predictVehicleCarbonDioxide

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
    if request.method == "POST":
        data = request.POST

        plant_species = data['plant_species']
        plant_species = plant_species.strip().capitalize()
        light_intensity = data['light_intensity']
        carbon_emission = data['carbon_emission']
        temperature = data['temperature']
        ans = predictOxygenEmission(plant_species=plant_species, light_intensity=light_intensity, carbon_emission=carbon_emission, temperature=temperature)

        oxygen_model = Oxygen_Emission(plant_species=plant_species, light_intensity=light_intensity, carbon_emission=carbon_emission, temperature=temperature, user=request.user, oxygen_emission=ans)
        oxygen_model.save()
        
        messages.info(request, f'Prediction= {ans}')
        return redirect('oxygen_emission')
    return render(request, 'mainapp/oxygen_emission.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def homeappliances(request):
    if request.user.is_admin:
            return redirect('adminuser')
    if request.method == "POST":
        data = request.POST

        appliance_type = data['appliance_type']
        appliance_type = appliance_type.strip().capitalize()
        electricity_units = data['electricity_units']
        age = data['age']
        maintenance = data['maintenance']

        ans = predictHomeApplianceCarbonDioxide(electricity_units, age, maintenance, appliance_type)

        # appliance_model = HomeAppliance_CO2_Emission(appliance_type=appliance_type, electricity_units=electricity_units, age=age, maintenance=maintenance, user=request.user, CO2_emissions=ans)
        # appliance_model.save()

        print(f'Prediction= {ans}')
        messages.info(request, f'Prediction= {ans}')
        return redirect('homeappliances')
    return render(request, 'mainapp/homeappliances.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def vehicles(request):
    if request.user.is_admin:
            return redirect('adminuser')
    if request.method == 'POST':
        data = request.POST
        engine_type = data['engine_type']
        cylinders = data['cylinders']
        transmission = data['transmission']
        fuel_type = data['fuel_type']

        return redirect('vehicles')

    return render(request, 'mainapp/vehicles.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def waste(request):
    if request.user.is_admin:
            return redirect('adminuser')
    if request.method == 'POST':
        data = request.POST

        e_waste = data['e_waste']
        proper_disposal = data['proper_disposal']
        composting = data['composting']
        recycling = data['recycling']

        return redirect('waste')
    return render(request, 'mainapp/waste.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def leaderboard(request):
    if request.user.is_admin:
            return redirect('adminuser')
    return render(request, 'mainapp/leaderboard.html')