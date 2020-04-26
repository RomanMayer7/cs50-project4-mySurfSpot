# Final Project 

Web Programming with Python and JavaScript

Project Name :"my Surf Spot"

Demo Video Link :https://www.youtube.com/watch?v=KHwLHBtZ0Fc

Project Objective
----------------------------------------------------------------------------------------
Gain experience with designing and implementing a Web application with Python\Django Framework and JavaScript,using HERE API for Geolocation.

Project Description
----------------------------------------------------------------------------------------
The aplication targets all Surfers and Surfing Lovers and helps them in ther search  
for best surfing spots located all around the globe ,and share them.They can add their comments,sharing their experience and opinions regarding every Surfing Spot.
They can join conversations on existing Spots and create their own Spots,providing location ,description and image URL of new Surfing Spot.Location of Surfing Spot will be shown through the Marker,spotting
on coordinates(longitude,latitude) on the Map Widget.User can zoom in and out
choosing his preferable view of Map Widget.Location of the Spot provided by user
in moment of Creation of New Surfing Spot record is interpreted into actual coordinates(longitude,latitude) with help of "HERE we go" API and shown on the Map Widget using API functionality provided inside appropriate JavaScript code snippet presented in page template.Application Implemented with usage Python + DJango.
technologies.Geocoder functionality implemented with help of "HERE API"
----------------------------------------------------------------------------------------

Project Structure
----------------------------------------------------------------------------------------
In [Project's Main Folder] there are:

*'db.sqlite3' file wich is used for Database Storage
*'manage.py' is used to Run Django Server and start our WEB Application
*'README.md' is current file where i describe my Project
*'requirements.txt' contains description
of all essential modules to be installed in order to run the App
*imports_and_testing.txt contains some data that you can import into DB
 in order to start using and testing APP

In [mysite] subfolder there are:
'settings.py' ,'urls'.py '_init_.py','wsgi.py'
responsibal gor all global project level related info

*In 'urls'.py there  are routs for application level local
urls :path('',include('surfspot.urls'))
as  well  for  admin maagement site:
path('admin/', admin.site.urls)

*'settings.py' have all properties of project
such Language Info and Codes

*A  Path for Database Connection(in our case we use a local lightweight version of SQL:"SQLite3")

*It also includes the information regarding all the applications installed in Project:
including our "Surfspot" Application 
and ADMIN SITE APP

INSTALLED_APPS = [
    'surfspot.apps.SurfspotConfig',
    'django.contrib.admin',
    'django.contrib.auth',
............]

[surfspot] subfolder contains all application specific data

*'models.py' contains all models for data types ,used in our App :"Spots","Messages"

*'views.py' contains all application  BackEnd logic written in Python
'Views' or Functions for all different routs the user can take when using the App
It prepares all the  nescessary data to represent it  inside different HTML Templates
when user chooses his route.

*'urls.py' listss all possible routs presented in Application with references to all appropriate views for each of them

*'admin.py' contains all registrations for different DB models  reserved for Admin Management Site

[templates] subfolder conatains all HTML Template files for every 'view' of application:
*'base.html' is main template from which all templates inheriting their basic template 
*and all the rest: 'spots.html','newspot.html','spotview.html','login.html'

[static] subfolder contains all images and stylesheet files used in App

[migrations] subfolder contains all migration 'py' files  which are  corresponds  to changes preformed in App's Datatabase 

Functionalities and their Implementation
----------------------------------------------------------------------------------------
[Project Requirements]
As per Project Requirements
'my Surf Spot' Web Application utilizing  Python, JavaScript, and SQL.
'my Surf Spot' Web Applicationmust is mobile-responsive.
Implemented with usage of responsive grids,relative dimensions,viewports and flexboxes

[Viewing Surf Spots]
Initialy after succesefully logging in ,user will see all
available Surf Spots rendered inside "spots.html" template
after clicking on one of them he rederected to "def spotview(request,spot_id):"
The view data is prepared in "def spotview(request,spot_id):"
back end function declared inside views.py and rendered
inside spotview.html template,The Spot Location
is shown inside Map Widget with help of appropriate JavaScript code snippet.

[Creating New Surf Spots]
The Data required in new Surf Spot Creation Process
is provided by user via form rendered as "newspot.html"
and this POST reqauest is sended into "def createspot(request):"
Back End function.There new Spot data is Added into DB via
appropriate ORM update command

[Geocoder functionality\Map Widget ]
Geocoder functionality implemented with help of "HERE API"
All API related javascript code is placed inside "spotview.html"
In order to use API functionality user must get
 'APP_ID' and 'APP_CODE' from https://www.here.com/
to set them as appropriate OS environmental variables.

[Comment Section ]
*Users can communicate inside each Surf Spot page by sending
their comments into page Comment Section.
New Comment is sended via AJAX HTTP request into "def addcomment(request):"
Back End function ,there it add into DB,via ORM.
After that the DOM is updated accordingly with appropriate requests 
inside Java Script Code

*User can remove only his own comments.Implemented by comparing current user
with message creator inside JavaScript code in "spotview.html"
After succesefull check the remove request is sended via AJAX
into "def removecomment(request):" Back End function,
there it removed into DB,via ORM.After that the DOM is updated accordingly
with appropriate requests inside JavaScript Code

[Using Django Admin]:Site Administrators able to add,update, and remove
 Surf Spots and user messages through Admin UI with Admin App installed on Project via localhost\admin route

[Registration, Login, Logout]: Application users  are  able to register for our web application with
 a username, password,first name, last name, and email address.
Implemented via extension of 'UserCreationForm' inside SignUpForm with addition
of apropriate fields.
Usera  are be able to log in and log out of your website.
This functionalities are implemented through
 def signup(request),'def login_view(request)' and 'def logout_view(request) '
  inside 'views.py'and rendered inside 'login.html' template


Database  populated with initial info via Shell Console with following command list
----------------------------------------------------------------------------------------

s=Spot(title='Bells Beach',location='Bells Beach,VIC,Australia',description='
Located around 100 km from Melbourne, Bells Beach is a historical and spiritual surf competition centre
 since 1961.It offers a powerful southerly swell and waves of over 5 meters. 
The home of Australian surfing is not only a spot to surf pumping and high-quality waves but also 
entertainment for those who love watching the surfers and its natural beauty.',
image='Bells Beach-VIC.jpg',creator='romanm')

s.save()

s=Spot(title='Gold Coast',location='Gold Coast,QLD,Australia',description='
Even it is far from being a secret surf point, surfrom all over the world with its warm weather all year long and a variety of waves
types.You can  find there the famous "superbank" at Kirra,incredible waves at Rainbow Bay,
Snapper Rocks and Narrowneck, to name a few. Welcome to the land of surf!',
image='Gold Coast-QLD.jpg',creator='romanm')
s.save()

s=Spot(title='Margaret River',location='Margaret River,WA,Australia',description='
This is definitely not a place for beginners. The wine region of Margaret River, situated at just 3 hours 
drive south from Perth, has also a surf lifestyle and different point breaks to go surfing.
In Prevelly Bay you can find swells producing 6 meters waves, we recommend going there
in case you are a serious pro and wear a helmet, safety first! However, other levels of surfers can
 enjoy the waves of Yallingup, a more democratic spot.',image='
Margaret River-WA.jpg',creator='romanm')
s.save()


s=Spot(title='Byron Bay',location='Byron Bay,NSW,Australia',description='
Byron Bay has something for everyone who wants to surf,  and definitely is one of the 7 best surf 
spots in Australia. The most famous and the best surf point out there, The Pass, offers one of the best
 right-hand breaks on the North Coast of NSW. Although it can be a bit crowded, we absolutely recommend
 going up to the surfer’s lookout where you can check the entire bay and choose the best spot to go.',
image='Byron Bay- NSW.jpg',creator='romanm')
s.save()

s=Spot(title='Northern Beaches',location='Northern Beaches,NSW,Australia',description='The Northern Beaches area of Sydney has 20 km of coastline, starting on Manly going to Palm Beach, 
with many beaches on the way to choose from.
Manly offers some surf schools for the ones who are willing to learn, check it out in our last post here.
North Narrabeen is our favourite surf spot there, with powerful waves and occasional strong swell. 
Long lefts or right barrels, depending on the swell, in 3 km of beach is just amazing!',
image='Northern Beaches-NSW.jpg',creator='romanm')
s.save()

s=Spot(title='Noosa Heads',location='Noosa Heads,QLD,Australia',description='Home of the best surf spots in calm waters, Noosa Heads is a great choice for both beginners 
or pro riders looking for a 200 meters ride. It is a really good place for longboarding as the area 
is protected from the wind and offers glassy and fun waves. Go for the breaks of Tea Tree Bay and
 Granite Bay, you will love it!',image='Noosa Heads-QLD.jpg',creator='romanm')
s.save()

s=Spot(title='Crescent Head',location='Crescent Head,NSW,Australia',description='Just a few hours drive from Sydney, Crescent Head has waves for every level of surfers and some 
of the longest breaks in the world. Ideal for longboarding with right-hand waves with up to 200 meters 
long.Crescent Head is a surfing reserve with protected marine life and a 60’s surf community, 
an absolute must go!',image='Crescent Head-NSW.jpg',creator='romanm')
s.save()

s=Spot(title='Central Coast',location='Central Coast,NSW,Australia',description='Its location halfway between Sydney and Newcastle is convenient for day-trippers, but that’s not the only reason Central Coast 
is one of Australia’s most popular surf destinations. Check out these beaches for reliable waves for all experience levels.
Avalon Beach. Just 45km north of Sydney, this beach has waves from beginner to expert level, and longboarders love it, too. 
It’s also produced champions like Ben Player—no big deal.
Fuel up: The Kiosk at Avalon on the Beach opens at 7am to feed the dawn patrol.
Wind down: The Surf Lounge at Avalon Beach RSL Club is open ‘til 2am on weekends.
Copacabana Beach. Save this one for the pros—this beach’s ledge breaks form powerful, hollow waves that really rip.
Head to the Bonnie Lookout if you just want to watch.
Fuel up: Allagai Bay Café serves up hearty brekkies like croissant French toast.
Wind down: Sundowners Bar & Grill has the only tap beer in the area—enough said.',image='Central Coast-NSW.jpg',creator='romanm')
s.save()

s=Spot(title='Exmouth',location='Exmouth,WA,Australia',description='Exmouth may be best known for Ningaloo Reef and swimming with whales, but surfers know it for its beautiful coastline 
and gnarly waves. It’s a great home base for exploring legendary spots like The Bommie, a left-handed ride on the 
peninsula’s northern tip. Beginners can hook up with Exmouth Surf Centre and head to Wobiri Access Beach for lessons.
Fuel up: Get your protein on with a breakfast wrap from Ningaloo Bakehouse & Café.
Wind down: Live tunes and cold brews flow at Froth Craft Restaurant in the evenings.',image='Exmouth-WA.png',creator='romanm')
s.save()

s=Spot(title='Yamba',location='Yamba,NSW,Australia',description='
A stay in picturesque Yamba puts you in perfect proximity to some world-famous breaks. 
At Turners Beach, Mother Nature provides both left-hand breaks at the northern end, and rights at the southern end, 
while Yamba-Angourie Surf School provides the lessons for those just starting out. 
Nearby Angourie Point is a well-known right-hand point break, made famous by legend Nat Young.
Fuel up: Order the Big Breakfast at Pippi’s Café, and you’ll be set for the day.
Wind down: Keep the ocean theme going with oysters or salmon at Pacific Bistro.',image='Yamba-NSW.jpg',creator='romanm')
s.save()

s=Spot(title='Kiama',location='Kiama,NSW,Australia',description='First things first—stop in to see the friendly folks at Zink Surf to gear up and get some advice from a local.
They might tell you to go north to The Farm in Killalea State Park, designated a National Surfing Reserve in 2009.
 Or, hit Werri Beach to the south for fun, clean breaks, good longboarding waves, and of course, the famous Werri Beach Fish Shop.
Fuel up: The Hungry Monkey was awarded “Most Outstanding Café” by the local business association.
Wind down: El Corazon’s specials, like $3 tacos and tequila shots on Tuesdays, make it a popular spot.',image='Kiama-NSW.jpg',creator='romanm')
s.save()

s=Spot(title='Kalbarri',location='Kalbarri,WA,Australia',description='In the vastness of Western Australia, 6 hours is a pretty short road trip—and that’s how long it takes to get from Perth to Jakes Point,
 in Kalbarri. This storied left-hand wave breaks for up to 200m and frequently reaches 5m high … so it goes without saying that this 
one is for the pros. The experts at Kalbarri Jetty Surf can get you kitted out with all the latest gear.
Fuel up: Bean Drifting café is right on Jakes Point, with all the sweet views you’d expect.
Wind down: Head into Kalbarri for dinner at Dirt Dust N Diesels Outback Restaurant.',image='Kalbarri-WA.jpg',creator='romanm')
s.save()


--------------------------------------------------------------------------
by Roman Meyerson @ 2019/Started:Mar 5, 2019-Finished:Mar 7, 2019
    
