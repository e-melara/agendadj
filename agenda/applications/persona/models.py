#
from model_utils.models import TimeStampedModel
#
from django.db import models
from .managers import ReunioManager


class Hobby(TimeStampedModel):
    hobby = models.CharField("Pasatiempos", max_length=50)

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"
       
    def __str__(self):
        return "{}-{}".format(self.id, self.hobby)
   

class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres',
        max_length=100,
    )
    job = models.CharField(
        'Trabajo',
        max_length=50,
        blank=True
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=20,
        blank=True,
    )

    hobbies = models.ManyToManyField(Hobby)
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
 
    def __str__(self):
        return "{}-{}".format(self.id, self.full_name)


class Reunion(models.Model):
    persona = models.ForeignKey(Person, on_delete=models.CASCADE)
    fecha = models.DateField("Fecha")
    hora = models.TimeField("Hora")
    asunto = models.CharField("Asunto de la reunion", max_length=100)
   
    objects = ReunioManager()
   
    class Meta:
        verbose_name = ("Reunion")
        verbose_name_plural = ("Reunions")
       
    def __str__(self):
        return "{}-{}-{}".format(self.persona.full_name, self.asunto, self.hora)
