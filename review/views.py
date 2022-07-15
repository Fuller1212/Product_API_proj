from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from review.models import Review
from review.serializers import ReviewSerializer
from django.db import models
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['Get'])
def review_list(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])      
def review_detail(request, pk):
        review = get_object_or_404(Review, pk=pk)
        if request.method == 'GET': 
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)