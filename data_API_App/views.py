##################################################################################
###############    FOREIGN CLASS IMPORTATIONS   #################################
################################################################################
from django.shortcuts import render
from data_API_App.models import Data_base, Shop
from rest_framework.response import Response
from data_API_App.serializer import DataSerializer, ShopSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
##################################################################################
###############    VIEW FUNCTIONALITY   ########################################
################################################################################
@api_view(['GET'])
def data_list(request):
    data_obj = Data_base.objects.all()
    serialized = DataSerializer(data_obj, many=True)
    return Response(serialized.data)

###############################    
@api_view(['POST'])
def data_create(request):
    serialized = DataSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data)
    else:
        return Response(serialized.errors)#, status=status.HTTP_400_BAD_REQUEST

@api_view(['GET','PUT','DELETE'])
def data_comb(request, pk):
    try:
        data_obj = Data_base.objects.get(pk=pk)
        return data_obj
    except:
        return Response({
            'error':'Book does not exist',          
        }, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':        
        serialized = DataSerializer(data_obj)
        return Response(serialized.data)
    if request.method == 'PUT':      
        serialized = DataSerializer(data_obj, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)      
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE': 
       data_obj.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
