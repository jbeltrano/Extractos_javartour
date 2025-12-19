from django.db import models

class Extracto(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    empresa = models.ForeignKey('Persona', related_name='extractos_empresa', on_delete=models.CASCADE)
    contrato = models.IntegerField()
    contratante = models.ForeignKey('Persona', related_name='extractos_contratante', on_delete=models.CASCADE)
    objeto_contrato = models.TextField()
    recorrido = models.TextField()
    convenio = models.ForeignKey('Convenio', on_delete=models.CASCADE)
    conductor_1 = models.ForeignKey('Conductor', related_name='conductor_1', on_delete=models.CASCADE)
    conductor_2 = models.ForeignKey('Conductor', related_name='conductor_2', on_delete=models.CASCADE, null=True, blank=True)
    conductor_3 = models.ForeignKey('Conductor', related_name='conductor_3', on_delete=models.CASCADE, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    responsable = models.ForeignKey('Persona', related_name='extractos_responsable', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Extracto'
        managed = False