import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room, Message
from a_users.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"  # اسم المجموعة

        # إضافة المستخدم إلى المجموعة
        await self.channel_layer.group_add(
            self.room_group_name,  # تصحيح التسمية
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # إزالة المستخدم من المجموعة
        await self.channel_layer.group_discard(
            self.room_group_name,  # تصحيح التسمية
            self.channel_name
        )

    async def receive(self, text_data):
        # استلام البيانات
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        # إرسال البيانات إلى جميع المستخدمين في المجموعة
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room
            }
        )

        # حفظ الرسالة في قاعدة البيانات
        await self.save_message(username, room, message)

    async def chat_message(self, event):
        # إرسال الرسالة إلى WebSocket
        message = event['message']
        username = event['username']
        room = event['room']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        # حفظ الرسالة في قاعدة البيانات
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        Message.objects.create(user=user, room=room, content=message)
