from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatUser, ChatMessage

def chat_room(request):
    return render(request, 'chat/chat_room.html')

def enter_chat(request, username):
    user, created = ChatUser.objects.get_or_create(name=username)
    return JsonResponse({'user_id': user.id})

def send_message(request, user_id, message):
    user = ChatUser.objects.get(id=user_id)
    ChatMessage.objects.create(user=user, content=message)
    return JsonResponse({'status': 'ok'})

# chat/views.py
from django.shortcuts import render

def chat_room(request):
    return render(request, 'chat/chat_room.html')

def video(request):
    return render(request, 'chat/video.html')

