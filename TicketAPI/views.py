from django.shortcuts import render
from .forms import TicketForm,LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
	return render(request,'base.html')

def login(request):

	form=LoginForm(request.POST or None)

	if form.is_valid():
		data=form

		

	return render(request,'registration/login.html',{'form':form})



   	#return render(request,'registration/login.html',{'form1':form1})
   	#return render(request,'registration/login.html',{'form1':form1})
@login_required
def submit_ticket(request):	

	form=TicketForm(request.POST or None)

	if form.is_valid():
		data=form.save()
		data.save()

		
	return render(request,'ticketapi/ticket_form.html',{'form':form})












