from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path("chat/", views.ChatList.as_view()),
	path("chat/<str:chat_uuid>/", views.ChatDetails.as_view()),
	path("message/", views.MessageList.as_view()),
	path("message/<str:message_uuid>/", views.MessageDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)