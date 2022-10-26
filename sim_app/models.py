from django.db import models

# Create your models here.

class SimNetwork(models.Model):
    sim_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.sim_name

class PhoneNumber(models.Model):
    sim_network = models.ForeignKey(SimNetwork, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=50, default="phone number")

    def __str__(self):
        return self.phone_number