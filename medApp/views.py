from django.shortcuts import render
from rest_framework import viewsets
from .models import Medecin
from .serializers import MedecinSerializer


# Create your views here.
class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer
