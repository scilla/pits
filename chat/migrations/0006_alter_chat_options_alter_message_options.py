# Generated by Django 5.0.4 on 2024-05-05 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0005_alter_chat_uuid_alter_message_uuid"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="chat",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="message",
            options={"ordering": ["-created_at"]},
        ),
    ]
