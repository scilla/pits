import random
from django.test import TestCase

from ..models import Chat, Message


class ChatTestBase(TestCase):
    def setUp(self):
        self.chat_1 = Chat.objects.create()
        self.chat_2 = Chat.objects.create()
        self.message_1 = Message.objects.create(content="Hello, world!", chat=self.chat_1, is_human=True)
        self.message_2 = Message.objects.create(content="Hello, computer!", chat=self.chat_1, is_human=False)