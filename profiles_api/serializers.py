from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Serializers a name field for a testing our APIView"""
    name = serializers.CharField(max_length=10)
