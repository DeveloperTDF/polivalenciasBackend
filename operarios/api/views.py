from rest_framework import generics
from operarios.api.serializers import OperarioSerializer
from operarios.models import Operario

class OperarioList(generics.ListCreateAPIView):
    queryset            =   Operario.objects.all()
    serializer_class    =   OperarioSerializer

class OperarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            =   Operario.objects.all()
    serializer_class    =   OperarioSerializer