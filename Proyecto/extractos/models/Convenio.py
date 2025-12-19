from django.db import models

class Convenio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'Convenio'
        managed = False
    
    def __str__(self):
        return self.nombre
