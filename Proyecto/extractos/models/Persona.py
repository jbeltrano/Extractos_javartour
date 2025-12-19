from django.db import models

class Persona(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    tipo_id = models.CharField(max_length=4)
    nombre = models.TextField()
    telefono = models.TextField()
    direccion = models.TextField()
    
    class Meta:
        db_table = 'Persona'
        managed = False