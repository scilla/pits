import os
from django.shortcuts import redirect
from openai import OpenAI
from rest_framework import generics

from pits.settings import OPENAI_API_KEY
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from .tools.ai import AI_PROMPT, MOCK_RESPONSE
from rest_framework.response import Response
from rest_framework import status

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
	
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		human_message = Message.objects.get(uuid=serializer.data["uuid"])
		chat_messages = Message.objects.filter(chat__uuid=serializer.data["chat"])
		formatted_messages = get_formatted_messages(chat_messages)
		completion = get_completion(formatted_messages)
		ai_answer = Message.objects.create(
			chat=Chat.objects.get(uuid=serializer.data["chat"]),
			content=completion,
			is_human=False,
		)
		human_message.reply = ai_answer
		human_message.save()
		headers = self.get_success_headers(serializer.data)
		return Response(MessageSerializer(human_message).data, status=status.HTTP_201_CREATED, headers=headers)


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = "uuid"
	queryset = Message.objects.all()
	serializer_class = MessageSerializer

def get_formatted_messages(messages):
	return [
		{
			"role": "user" if message.is_human else "assistant",
			"content": message.content,
		}
		for message in messages
	]


def get_completion(formatted_messages):
	if "mock" in formatted_messages[-1]["content"]:
		return MOCK_RESPONSE
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

