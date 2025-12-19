from django.shortcuts import render, get_object_or_404
from .models.Extracto import Extracto

def detalle_extracto(request, extracto_id):
    """
    Vista para mostrar el detalle de un extracto por su ID
    """
    extracto = get_object_or_404(Extracto, id=extracto_id)
    
    context = {
        'extracto': extracto
    }
    
    return render(request, 'extractos/detalle_extracto.html', context)
