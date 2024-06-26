from .base import ChatTestBase
from rest_framework.test import RequestsClient
from unittest.mock import patch

def mocked_openai_response(formatted_messages):
	return "This is a mocked ai response!"

class ChatViewsTests(ChatTestBase):
	client = RequestsClient()

	def test_chat_list(self):
		response = self.client.get(f"/chat/").json()
		self.assertEqual(response[0]["messages_count"], 2)
		self.assertEqual(response[1]["messages_count"], 0)
	
	def test_chat_details(self):
		response = self.client.get(f"/chat/{self.chat_1.uuid}/").json()
		self.assertEqual(response["messages_count"], 2)
	
	def test_chat_messages_list(self):
		response = self.client.get(f"/chat/{self.chat_1.uuid}/messages/").json()
		self.assertEqual(len(response), 2)
		self.assertEqual(response[0]["content"], "Hello, world!")
	
	def test_message_list(self):
		response = self.client.get(f"/message/").json()
		self.assertEqual(len(response), 2)
	
	def test_message_details(self):
		response = self.client.get(f"/message/{self.message_1.uuid}/").json()
		self.assertEqual(response["content"], "Hello, world!")
	