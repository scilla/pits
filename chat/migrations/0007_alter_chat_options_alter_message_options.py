# Generated by Django 5.0.4 on 2024-05-05 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0006_alter_chat_options_alter_message_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="chat",
            options={"ordering": ["created_at"]},
        ),
        migrations.AlterModelOptions(
            name="message",
            options={"ordering": ["created_at"]},
        ),
    ]