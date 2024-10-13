from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CRUDS
from .serializers import productSerializer
from django.db.models import Q

# Create your views here.

@api_view(['GET','POST','DELETE'])
def show_all(request):
    pro=CRUDS.objects.all()
    if request.method == 'GET':
        pro=CRUDS.objects.all()
        sr=productSerializer(pro,many=True)
        return Response(sr.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        sr=productSerializer(data=request.data)
        if sr.is_valid():
            sr.save()
            return Response(sr.data,status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        pro.delete()
        pro2=CRUDS.objects.all()
        sr=productSerializer(pro2,many=True)
        return Response(sr.data,status=status.HTTP_200_OK)
@api_view(['GET','PUT','DELETE'])
def single_obj(request,pk):
    try:
        pro=CRUDS.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        sr=productSerializer(pro)
        return Response(sr.data,status=status.HTTP_200_OK)
    elif request.method =='DELETE':
        pro.delete()
        pro2=CRUDS.objects.all()
        sr=productSerializer(pro2,many=True)
        return Response(sr.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        sr=productSerializer(pro,data=request.data)
        if sr.is_valid():
            sr.save()
            return Response(sr.data)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def search(request,text):
    
    obj=CRUDS.objects.distinct().filter(
             Q(title__icontains=text)|
             Q(total__icontains=text) |
             Q(category__icontains=text)
    )
    
    sr=productSerializer(obj,many=True)
    return Response(sr.data,status=status.HTTP_200_OK)
