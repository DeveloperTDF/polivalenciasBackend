from rest_framework import serializers
from operarios.models import Operario

class OperarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operario
        fields = ['id', 'legajo', 'nombre', 'puesto']
