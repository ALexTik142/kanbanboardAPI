from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):                           #Сериалайзер для модели Task
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) #Автоматическая связь с авторизованным пользователем
    class Meta:
        model = Task
        fields = "__all__"