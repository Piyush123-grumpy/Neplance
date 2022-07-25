from multiprocessing import context
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from requests import Session
from account.models import User
from chatsystem.models import session,participants,message

# Create your views here.
def chatlist(request):
    a=request.user.getRoom()
    context={"Session":a}
    return render(request,'chat_list.html',context)

def create_session(request,name):
    participant1=request.user.username
    participant2=User.objects.get(username=name)
    session_name_from_employerside=f'{participant1} and {participant2.username}'
    session_name_fromfreelancerside=f'{participant2.username} and {participant1}'
    if request.user.is_employer:
        if session.objects.filter(name=session_name_from_employerside).exists():
            return redirect('/chatlist')
        else:
            Session=session.objects.create(name=participant1+" and "+participant2.username)
            Session.save()
            Participants1=participants.objects.create(session=Session,user=request.user)
            Participants1.save()
            Participants2=participants.objects.create(session=Session,user=User.objects.get(username=name))
            Participants2.save()

    else:
        if session.objects.filter(name=session_name_fromfreelancerside).exists():
            return redirect('/chatlist')
        else:
            Session=session.objects.create(name=participant2.username+" and "+participant1)
            Session.save()
            Participants1=participants.objects.create(session=Session,user=request.user)
            Participants1.save()
            Participants2=participants.objects.create(session=Session,user=User.objects.get(username=name))
            Participants2.save()
            
    
    return redirect('/chat')
   
def chat(request,name):
    Session=session.objects.get(name=name)
    Message=message.objects.filter(session=Session)
    user=request.user
    a=request.user.getRoom()
    context={"participant":a,"Message":Message,'user':user,'Session':Session}
    return render(request,'chat.html',context)

def send(request):
    username=request.POST["username"]
    Message=request.POST["message"]
    session_name=request.POST["sessionid"]
    Session=session.objects.get(name=session_name)
    new_message=message.objects.create(session=Session,user=username,message=Message)
    new_message.save()
    return HttpResponse("Okay!!!")

def get_message(request,name):
    Session=session.objects.get(name=name)
    Message=message.objects.filter(session=Session)

    return JsonResponse({'messages':list(Message.values()),'okay':"cool"})


