from django.urls import path
from . import views

app_name = 'extractos'

urlpatterns = [
    path('<str:extracto_id>', views.detalle_extracto, name='detalle_extracto'),
]
