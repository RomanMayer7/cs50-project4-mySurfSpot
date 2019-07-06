from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from .models import Spot,Message

from django.shortcuts import redirect

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import json,os

class SignUpForm(UserCreationForm):
 first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
 last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
 email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
 class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        form = SignUpForm()
        return render(request, "surfspot/login.html", {"form":form,"message": None})
    context = {
        "user": request.user,
        "spots": Spot.objects.all()
    }
    return render(request, "surfspot/spots.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        form = SignUpForm()
        return render(request, "surfspot/login.html",{"form":form,"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    form = SignUpForm()
    return render(request, "surfspot/login.html",{"form":form,"message": "Invalid credentials."})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
     form = SignUpForm()
     return render(request, "surfspot/login.html",{"form":form,"message": "Invalid Sign UP Attempt."})

def spots(request):
     context = {
     "user": request.user,
     "spots": Spot.objects.all()}
     return render(request, "surfspot/spots.html",context)

#create view of all Surfing Spots in Database
def spotview(request,spot_id):
    #get environment variables for HERE WE GO API
    api_id=os.environ.get('APP_ID')
    api_code=os.environ.get('APP_CODE')
    #get Spot Data
    spot=Spot.objects.filter(id=spot_id)
    comments=Message.objects.filter(spot=spot_id)
    #preparre the context for request
    context = {
	"user": request.user,
    "spot_id":spot[0].id,
	"title":spot[0].title,
	"description":spot[0].description,
	"comments":comments,
	"image":spot[0].image,
	"location":spot[0].location,
    "api_id":api_id,
    "api_code":api_code
	}
    return render(request, "surfspot/spotview.html",context)


#rendering a form to collect data nescessary for the new Spot creation
def newspot(request):
 context = {"user": request.user}
 return render(request,"surfspot/newspot.html",context)


#defining function to create new Surfing Spot
def createspot(request):
    #Getting user info
    user=request.user
    #full_name=""+user.first_name+" "+user.last_name
    #getting data from the form
    title = str(request.POST["title"])
    location = str(request.POST["location"])
    description = str(request.POST["description"])
    image = str(request.POST["image"])
	#Add new Surf Spot to Database 
    s=Spot(title=title,location=location,description=description,image=image,creator=user)
    s.save()
    return HttpResponseRedirect(reverse("index"))

#This can be called by AJAX request
@csrf_exempt
def addcomment(request):
 #Getting user info
 #user=request.user
 
 user = str(request.POST["m_creator"])
 spot_id = int(request.POST["spot_id"])
 date = str(request.POST["m_date"])
 content = str(request.POST["m_content"])
 #print("WE GOT HERE!!")
 #print(content)
 #Add new Comment to Database 
 msg=Message(content=content,date=date,creator=user,spot=spot_id)
 msg.save()
 return HttpResponse(json.dumps({"success":True}), content_type="application/json")
  

#This can be called by AJAX request
@csrf_exempt	
def removecomment(request):

   message_id = int(request.POST["removed_id"])

   msg=Message.objects.filter(id=message_id)
   msg[0].delete()
   return HttpResponse(status=204)


#---------------------------------------------------------------
#This can be called by AJAX request	
#This functionality currently not availabale
#(Decided to restrict users from deleting spots on this stage)
def removespot(request):

   spot_id = int(request.POST["spot_id"])
   #print("Number of Spot to be  removed:")
   #print(spot_id)
   spot=Spot.objects.filter(id=spot_id)
   spot[0].delete()
   return HttpResponse(status=204)
#------------------------------------------------------------































