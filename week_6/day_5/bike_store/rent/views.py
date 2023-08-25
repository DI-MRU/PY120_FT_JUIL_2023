from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rental
from .serializers import RentalSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class RentalList(APIView):

    def get(self, request, format=None):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RentalDetail(RetrieveUpdateDestroyAPIView):
    allrentalDetails = Rental.objects.all()
    serializer_class = RentalSerializer()

