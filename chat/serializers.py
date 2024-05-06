from rest_framework import serializers
from .models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["uuid", "created_at", "messages_count"]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["uuid", "content", "created_at", "chat", "is_human", "reply"]
