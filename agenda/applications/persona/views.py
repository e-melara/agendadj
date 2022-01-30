from django.views.generic import ListView

# django rest framework
from rest_framework.generics import ListAPIView

from .models import Person
from .serializers import PersonSerializer


class ListaPersonaListView(ListView):
    context_object_name = "personas"
    template_name = "persona/personas.html"
    
    def get_queryset(self):
        return Person.objects.all()
    
class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer
    paginate_by = 10
    def get_queryset(self):
        return Person.objects.all()
    
