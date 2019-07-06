from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
    path("spots",views.spots,name="spots"),
    path("newspot",views.newspot,name="newspot"),
    path("createspot",views.createspot,name="createspot"),
    path("removespot",views.removespot,name="removespot"),
	path("spotview\<int:spot_id>",views.spotview,name="spotview"),
	path("addcomment",views.addcomment,name="addcomment"),
	path("removecomment",views.removecomment,name="removecomment"),


]