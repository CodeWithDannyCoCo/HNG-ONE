from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NumberClassificationSerializer

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
        
        # Use serializer to process the number
        serializer = NumberClassificationSerializer(number)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            "error": True,
            "message": "Internal server error"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
