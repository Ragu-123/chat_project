from django.urls import path
from .views import chat_room, enter_chat, send_message

urlpatterns = [
    path('', chat_room, name='chat_room'),
    path('enter_chat/<str:username>/', enter_chat, name='enter_chat'),
    path('send_message/<int:user_id>/<str:message>/', send_message, name='send_message'),
]
