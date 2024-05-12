from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Task
from .permissions import IsAdminOrReadOnly, IsUserOrReadOnly
from .serializers import TaskSerializer




class TaskAPIList(generics.ListAPIView):                    #Представление для чтения всего списка (с общим доступом)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAPIListCreate(generics.ListCreateAPIView):       #Представление для чтения всего списка и добавления (для авторизованных пользователей)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TaskAPIReadOneEntry(generics.RetrieveAPIView):      #Представление для чтения одной записи (для авторизованных пользователей)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TaskAPIUpdate(generics.RetrieveUpdateAPIView):     #Представление для изменения одной записи (для пользователя , который добавил запись)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsUserOrReadOnly, )

class TaskAPIDestroy(generics.RetrieveDestroyAPIView):   #Представление для удаление одной записи (только для админа)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminOrReadOnly, )