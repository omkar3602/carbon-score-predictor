from mainapp.models import Carbon_Score

def get_carbon_score(oxygen_val, home_appliance_co2_val, vehicle_co2_val, waste_management_co2_val, user):
        mean_co2_emission = (home_appliance_co2_val+vehicle_co2_val+waste_management_co2_val)/3
        
        net_carbon_emission = mean_co2_emission - oxygen_val
        
        carbon_score_model = Carbon_Score(carbon_score=net_carbon_emission, user=user)

        carbon_score_model.save()