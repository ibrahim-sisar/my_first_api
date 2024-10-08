from rest_framework import serializers
from .models import CRUDS

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=CRUDS
        fields='__all__'