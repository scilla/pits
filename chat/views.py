import os
from django.shortcuts import redirect
from django.contrib.staticfiles import finders
from openai import OpenAI
from rest_framework import generics

from pits.settings import OPENAI_API_KEY
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from django.views.generic import TemplateView
from dotenv import load_dotenv
from .tools.ai import AI_PROMPT, MOCK_RESPONSE


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


def get_completion(formatted_messages):
	client = OpenAI(
		api_key=OPENAI_API_KEY,
	)
	chat_completion = client.chat.completions.create(
		messages=[
			{
				"role": "system",
				"content": AI_PROMPT,
			}
		]
		+ formatted_messages,
		model="gpt-3.5-turbo",
	)
	return chat_completion.choices[0].message.content


def get_AI_response(request, *args, **kwargs):
	chat_uuid = kwargs["uuid"]
	messages = Message.objects.filter(chat__uuid=chat_uuid)
	if "mock" in messages.last().content:
		ai_response = MOCK_RESPONSE
	else:
		formatted_messages = [
			{
				"role": "user" if message.is_human else "assistant",
				"content": message.content,
			}
			for message in messages
		]
		ai_response = get_completion(formatted_messages)
	res = Message.objects.create(
		chat=Chat.objects.get(uuid=chat_uuid),
		content=ai_response,
		is_human=False,
	)
	return redirect(f"/message/{res.uuid}/")
