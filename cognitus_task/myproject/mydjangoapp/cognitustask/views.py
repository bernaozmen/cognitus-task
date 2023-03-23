from email.policy import default
import re
from urllib import response
from django import views
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from .forms import DataForm
from .models import Data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions,generics
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import DataSerializer
import requests
import json
from django.conf import settings
from django.shortcuts import get_object_or_404

from cognitustask.helpers import Settings
# Create your views here.

class Train(APIView):
    def post(self,request):
        #url = "http://127.0.0.1:8000/train"
        response = requests.post(Settings.TRAIN_URI)
        return Response(response.json())

class Predict(APIView):
    def post(self,request):
        text = request.GET.get('text', False)
       # print(request.data)
        #url = "http://127.0.0.1:8000/predict"
       # url = "http://127.0.0.1:8070/predict?text="+ text
       # response = requests.post(url)
        response = requests.post(Settings.PREDICT_URI,json={"text": text})
        return Response(response.json())

"""class DataList(APIView):
    def get(self,request):
        datas=Data.objects.all()
        serializer = DataSerializer(datas,many=True) 
        return Response(serializer.data)

    def post(self):
        pass"""

class DataList(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data
    serializer_class = DataSerializer

"""def data_list(request):
    context = {'data_list':Data.objects.all()}
    return render(request,"cognitustask/data_list.html",context)
    

def data_form(request,id=0): #insert, update
    if request.method =="GET":
        if id==0:
            form = DataForm()
        else:
            data = Data.objects.get(pk=id)
            form = DataForm(instance=data)
        return render(request,"cognitustask/data_form.html",{'form':form})
    else:
        if id == 0:
            form = DataForm(request.POST)
        else:
            data = Data.objects.get(pk=id)
            form = DataForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect('/data/list')

def data_delete(request,id):
    data = Data.objects.get(pk=id)
    data.delete()
    return redirect('/data/list')
"""
