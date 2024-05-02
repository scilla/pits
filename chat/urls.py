from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path("chat/", views.ChatList.as_view()),
	path("chat/<str:uuid>/", views.ChatDetails.as_view()),
	path("message/", views.MessageList.as_view()),
	path("message/<str:uuid>/", views.MessageDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)