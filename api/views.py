from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NumberClassificationSerializer

# Create your views here.

@api_view(['GET'])
def classify_number(request):
    # Get number parameter from query string
    number = request.GET.get('number')
    
    # Handle missing number parameter
    if not number:
        return Response({
            "number": None,
            "error": True
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Try to convert to integer
    try:
        number = int(number)
    except (ValueError, TypeError):
        return Response({
            "number": number,
            "error": True
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Use serializer to process the number
        serializer = NumberClassificationSerializer(number)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        # Log the error here if you have logging configured
        return Response({
            "number": None,
            "error": True
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
