from django.views.generic import ListView

# django rest framework
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, 
    RetrieveDestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView
)

from .models import Person, Reunion
from .serializers import PersonSerializer, PersonaSerializer, ReunionSerializer


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
    

class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer
    

class PersonDetailView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.filter()
    
    
class PersonDeleteView(RetrieveDestroyAPIView):
    serializer_class = PersonSerializer
    queryset= Person.objects.all()
    
    
class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.filter()
    
    
class PersonUpdateRetrieve(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.filter()
    
    
class PersonApiListView(ListAPIView):
    serializer_class = PersonaSerializer
    
    def get_queryset(self):
        return Person.objects.all()
    

class ReunionApiView(ListAPIView):
    serializer_class = ReunionSerializer
    
    def get_queryset(self):
        return Reunion.objects.all()
    

    