from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import is_prime, is_perfect, get_properties, get_digit_sum, get_fun_fact

# Create your views here.

@api_view(['GET'])
def classify_number(request):
    try:
        # Get number parameter from query string
        number = request.GET.get('number')
        if not number:
            return Response({
                "error": True,
                "message": "Please provide a number parameter"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Try to convert to integer
        try:
            number = int(number)
        except ValueError:
            return Response({
                "error": True,
                "message": "Invalid number format"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Get all properties
        response_data = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": get_properties(number),
            "digit_sum": get_digit_sum(number),
            "fun_fact": get_fun_fact(number)
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            "error": True,
            "message": "Internal server error"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
