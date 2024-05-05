from .base import ChatTestBase
from ..models import Chat, Message


class ChatModelsTests(ChatTestBase):
    def test_chat_was_created(self):
        chat_count = Chat.objects.count()
        self.assertEqual(chat_count, 2)

    def test_message_was_created(self):
        message_count = Message.objects.count()
        self.assertEqual(message_count, 2)

    def test_message_was_created_with_correct_content(self):
        message = Message.objects.first()
        self.assertEqual(message.content, "Hello, world!")
        self.assertEqual(message.is_human, True)
        self.assertEqual(message.chat, self.chat_1)

    def test_chat_has_messages(self):
        self.assertEqual(self.chat_1.messages_count, 2)
        self.assertEqual(self.chat_2.messages_count, 0)