from django.urls import path

from .views import (
    ListaPersonaListView, PersonListApiView, PersonCreateView, PersonDetailView, 
    PersonDeleteView, PersonUpdateView, PersonUpdateRetrieve, PersonApiListView, 
    ReunionApiView, PersonaPaginatorView, ReunionByPersonJob
)
app_name = 'personas_app'

urlpatterns = [
    # html
    path('lista-persona/', view=ListaPersonaListView.as_view(),name='lista-persona'),
    # api rest
    path('api/persona/list/', view=PersonListApiView.as_view(),name='api-persona-list'),
    path('api/persona/create/', view=PersonCreateView.as_view(),name='api-persona-create'),
    path('api/persona/<pk>/', view=PersonDetailView.as_view(),name='api-persona-detail'),
    path('api/persona/update/<pk>/', view=PersonUpdateView.as_view(),name='api-persona-update'),
    path('api/persona/modificar/<pk>/', view=PersonUpdateRetrieve.as_view(),name='api-persona-update-get'),
    path('api/persona/delete/<pk>/', view=PersonDeleteView.as_view(),name='api-persona-delete'),
    
    # serializer normales
    path('api/persona/list/serializer', view=PersonApiListView.as_view(),name='api-list-serializer'),
    # Reunion api view
    path('api/reunion/list', view=ReunionApiView.as_view(),name='api-list-reunion'),
    # pagination de persona
    path('api/persona', view=PersonaPaginatorView.as_view(),name='persona-list-pagination'),
    path('api/reunion/count', view=ReunionByPersonJob.as_view(),name='reunion-count-list'),
]
