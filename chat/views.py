from rest_framework import generics
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer

class ChatList(generics.ListCreateAPIView):
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer

class ChatDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer

class MessageList(generics.ListCreateAPIView):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer

class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer