from django.contrib import admin
from django.urls import path, include
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),           #Авторизация и куки
    path('api/v1/tasks/list/', TaskAPIList.as_view()),                  #Маршрут для чтения данных (Общий доступ)
    path('api/v1/tasks/create/', TaskAPIListCreate.as_view()),          #Маршрут для чтения данных и добавление записи(Авторизованным пользователям)
    path('api/v1/tasks/<int:pk>/', TaskAPIReadOneEntry.as_view()),      #Маршрут для чтения одной записи(Авторизованным пользователям)
    path('api/v1/tasks/update/<int:pk>/', TaskAPIUpdate.as_view()),     #Маршрут для изменения одной записи(Для пользователя , который добавил запись)
    path('api/v1/tasks/delete/<int:pk>/', TaskAPIDestroy.as_view())     #Маршрут для удаление одной записи(Для админа)
]
