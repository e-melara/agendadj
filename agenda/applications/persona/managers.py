from django.db import models
from django.db.models import Count

class ReunioManager(models.Manager):
    def cantidad_reunion(self):
        resultado = self.values(
            'persona__job'
        ).annotate(
            cantidad=Count('id')
        )
        
        return resultado