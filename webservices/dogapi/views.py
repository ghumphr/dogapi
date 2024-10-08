from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dog
from .models import Breed
from .serializers import DogSerializer
from .serializers import BreedSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# This code is from the initial REST test and is deprecated
#@api_view(['GET'])
#def rest_get_dog(request, dog_id):
#    try:
#        dog = Dog.objects.get(pk=dog_id)
#        serializer = DogSerializer(dog)
#        return Response(serializer.data)
#    except Dog.DoesNotExist:
#        return Response({'error': 'Dog not found.'}, status=status.HTTP_404_NOT_FOUND)
#
#
#@api_view(['GET'])
#def rest_get_breed(request, breed_id):
#    try:
#        breed = Breed.objects.get(pk=breed_id)
#        serializer = BreedSerializer(breed)
#        return Response(serializer.data)
#    except Breed.DoesNotExist:
#        return Response({'error': 'Breed not found.'}, status=status.HTTP_404_NOT_FOUND)


class DogList(APIView):
    """
    List all dogs, or create a new dog.
    """
    def get(self, request, format=None):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedList(APIView):
    """
    List all breeds, or create a new breed.
    """
    def get(self, request, format=None):
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    """
    Retrieve, update or delete a dog instance.
    """
    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, dog_id, format=None):
        dog = self.get_object(dog_id)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, dog_id, format=None):
        dog = self.get_object(dog_id)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, dog_id, format=None):
        dog = self.get_object(dog_id)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedDetail(APIView):
    """
    Retrieve, update or delete a breed instance.
    """
    def get_object(self, pk):
        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404

    def get(self, request, breed_id, format=None):
        breed = self.get_object(breed_id)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, breed_id, format=None):
        breed = self.get_object(breed_id)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, breed_id, format=None):
        breed = self.get_object(breed_id)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


