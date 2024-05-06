from django.contrib import admin


from .models import Chat, Message

class MessageInline(admin.TabularInline):
	model = Message

class ChatAdmin(admin.ModelAdmin):
	inlines = [MessageInline]

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message)
