from django.shortcuts import redirect
from rest_framework import generics
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from django.views.generic import TemplateView


class ChatList(generics.ListCreateAPIView):
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer


class ChatDetails(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = "uuid"
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer


class ChatMessagesList(generics.ListAPIView):
	serializer_class = MessageSerializer

	def get_queryset(self):
		return Message.objects.filter(chat__uuid=self.kwargs["uuid"])


class MessageList(generics.ListCreateAPIView):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = "uuid"
	queryset = Message.objects.all()
	serializer_class = MessageSerializer
