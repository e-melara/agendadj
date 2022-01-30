from django.urls import path

from .views import ListaPersonaListView, PersonListApiView

urlpatterns = [
    path('lista-persona/', view=ListaPersonaListView.as_view(),name='lista-persona'),
    path('api/persona/list/', view=PersonListApiView.as_view(),name='api-persona-list'),
]
