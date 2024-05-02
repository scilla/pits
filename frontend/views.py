from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from chat.models import Chat


class NewChatView(View):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        new_chat = Chat.objects.create()
        return redirect("chat_view", chat_uuid=new_chat.uuid)


class ChatView(TemplateView):
    template_name = "chat.html"
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        chat_uuid = self.kwargs.get("chat_uuid")
        chat = Chat.objects.get(uuid=chat_uuid)
        kwargs["chat"] = chat
        return super().get(request, *args, **kwargs)
