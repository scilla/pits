from uuid import uuid4
from django.db import models

class Chat(models.Model):
	uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["created_at"]

	def __str__(self):
		return f"Chat {self.uuid}"
	
	@property
	def messages_count(self):
		return self.messages.count()


class Message(models.Model):
	uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
	content = models.TextField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
	is_human = models.BooleanField()
	reply = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		ordering = ["created_at"]

	def __str__(self):
		return f"Message {self.uuid} in Chat {self.chat.uuid}"
