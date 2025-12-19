from django.db import models

class Conductor(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    nombre = models.TextField()
    vigencia = models.DateField()
    
    class Meta:
        db_table = 'Conductor'
        managed = False