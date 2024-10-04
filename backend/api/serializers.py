from django.cotrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} #only write password, dont want it to be read

    def create(self, validated_data):
         user = User.objects.create_user(**validated_data) #data passed by serailizer
         return user   