from django.shortcuts import render , redirect
from .models import Room ,Message
from django.contrib import messages
# Create your views here.

def rooms(request):
    rooms =Room.objects.all()
    context ={
        'rooms':rooms
    }
    return render(request, 'room/rooms.html',context)

def room(request ,  pk):
    room = Room.objects.get(name=pk)
    message = Message.objects.filter(room=room)
    context = {
       
        'room':room,
        'message':message,

    }
    return render(request, 'room/room.html',context)

def create_room(request):
    if request.method == 'POST':
        
        room_name = request.POST.get('room_name')
        description = request.POST.get('description')
        if request.user.is_authenticated :
            Room.objects.create(host=request.user,name =room_name,slug=description)
            
            return redirect('rooms')
        else :
            messages.error(request,'You are not logged in')

    return render(request, 'room/create-room.html')