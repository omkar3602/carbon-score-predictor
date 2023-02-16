from django.db import models
from userauth.models import Account
from django.utils import timezone

# Create your models here.
class Oxygen_Emission(models.Model):
    plant_species = models.CharField(max_length=30)
    light_intensity = models.DecimalField(..., max_digits=5, decimal_places=2)
    carbon_emission = models.DecimalField(..., max_digits=5, decimal_places=2)
    temperature = models.DecimalField(..., max_digits=5, decimal_places=2)

    submitted_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + "-" + self.submitted_on