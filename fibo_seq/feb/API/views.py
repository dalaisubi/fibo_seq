from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FibonacciSerializer

class Fibonacci(APIView):

    def post(self, request, *args, **kwargs):
    	serializers = FibonacciSerializer(data=request.data)
    	if serializers.is_valid(raise_exception=True):

	    	return Response(serializers.data, status=status.HTTP_200_OK)
    	return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

