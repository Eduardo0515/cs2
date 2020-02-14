# Create your models here.
from django.db import models
from django.utils import timezone

class ModelCiudad(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'ModelCiudad'

class ModelGenero(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'ModelGenero'

class ModelOcupacion(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'ModelOcupacion'

class ModelEstado(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'ModelEstado'
    

class ModelEstadoCivil(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'ModelEstadoCivil'

class ModelProfile(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apellidoP = models.CharField(max_length=254, null=False)
    apellidoM = models.CharField(max_length=254, null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(ModelCiudad,on_delete=models.CASCADE)
    genero = models.ForeignKey(ModelGenero,on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(ModelOcupacion,on_delete=models.CASCADE)
    estado = models.ForeignKey(ModelEstado,on_delete=models.CASCADE)
    estadoCivil = models.ForeignKey(ModelEstadoCivil,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'ModelProfile'
