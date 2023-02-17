import pickle

def predictOxygenEmission(plant_species,light_intensity, carbon_emission, temperature):
    with open('utils/Pickle_Files/label.pickle', 'rb') as handle:
        b = pickle.load(handle)
    model=pickle.load(open('utils/Pickle_Files/model.pkl', 'rb'))
    val=b.get(plant_species)
    ans=model.predict([[val,light_intensity, carbon_emission, temperature]])
    return ans[0]