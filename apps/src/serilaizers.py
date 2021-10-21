from rest_framework import serializers
from apps.src.models import Base


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = "__all__"


class BaseCodeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
