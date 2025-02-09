from django.urls import path
from django.http import JsonResponse
from . import views

def api_root(request):
    return JsonResponse({
        "message": "Number Classification API",
        "endpoints": {
            "classify_number": "/api/classify-number"
        }
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('classify-number', views.classify_number, name='classify-number'),
] 