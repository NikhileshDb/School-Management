from django.db import models

"""Transport Model"""
class transport(models.Model):
    transport_id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=500, null=True, blank=True)
    number_of_vehicle = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    route_fare = models.BigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.route_name

