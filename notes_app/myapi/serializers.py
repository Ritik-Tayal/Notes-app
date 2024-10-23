from rest_framework import serializers
from notes.models import Notes
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('__all__')
        