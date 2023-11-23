# chat_project/urls.py

from django.contrib import admin
from django.urls import path, include
from chat.routing import application as chat_application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('ws/', chat_application),  # Use chat_application directly
]
