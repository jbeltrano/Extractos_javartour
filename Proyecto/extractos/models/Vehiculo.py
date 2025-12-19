from django.db import models

class Vehiculo(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    modelo = models.TextField()
    marca = models.TextField()
    clase = models.TextField()
    interno = models.IntegerField()
    top = models.IntegerField()
    
    class Meta:
        db_table = 'Vehiculo'
        managed = False