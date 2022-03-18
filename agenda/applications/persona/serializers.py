from rest_framework import serializers, pagination

from .models import Person, Reunion, Hobby

class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = (
            'hobby',
            'id',
        )


class PersonSerializer(serializers.ModelSerializer):
    
    
    hobbies = HobbiesSerializer(many=True)
    
    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created'
        )
    
        
class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    
    
class ReunionSerializer(serializers.HyperlinkedModelSerializer):
  
    fecha_hora = serializers.SerializerMethodField()
    
    class Meta:
        model = Reunion
        fields = (
            'id', 
            'fecha', 
            'hora',
            'asunto',
            'persona',
            'fecha_hora',
        )
        
        extra_kwargs = {
            'persona': {
                'view_name' : 'personas_app:api-persona-detail',
                'lookup_field' : 'pk'
            }
        }
        
    def get_fecha_hora(self, object):
        return "{} - {}".format(object.fecha, object.hora)
    

class PersonaPaginator(pagination.PageNumberPagination):
    page_size = 5
    max_page = 100


class ReunionCountSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()