#
from model_utils.models import TimeStampedModel
#
from django.db import models


#
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


    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return "{}-{}".format(self.id, self.full_name)
