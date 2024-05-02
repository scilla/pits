from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.NewChatView.as_view(), name="new_chat_view"),
    path("<uuid:chat_uuid>/", views.ChatView.as_view(), name="chat_view"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
