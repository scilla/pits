from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path("chat/", views.ChatList.as_view(), name="chat-list"),
	path("chat/<uuid:uuid>/", views.ChatDetails.as_view(), name="chat-detail"),
	path("chat/<uuid:uuid>/messages/", views.ChatMessagesList.as_view(), name="chat-messages-list"),
	path("message/", views.MessageList.as_view(), name="message-list"),
	path("message/<uuid:uuid>/", views.MessageDetails.as_view(), name="message-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)