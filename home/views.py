from django.shortcuts import render, redirect
from emanjha_admin.models import Virtual, Activities, Facilities, Location_add, Categories,Usa_state, Covid_state_link, Park_tag,Guideline,Guideline_detail
from django.contrib.auth.models import User, auth
from .models import  *
import ast
from django.http import JsonResponse
import json, requests
import urllib.request
import time
import reverse_geocoder as rg
# pip install reverse_geocoder
import os
import pprint
import socket
# pip3 install js2py
from django.http import JsonResponse
from .mmail import tabmail
import random
from django.core.mail import BadHeaderError, send_mail
import datetime
from datetime import date
from GoogleNews import GoogleNews
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from math import sin, cos, sqrt, atan2, radians
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.db.models import Q
import csv
import googlemaps
import wikipedia
from .usa_models import state_review
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import logging
logger = logging.getLogger('django')
from PIL import Image
from io import BytesIO
# FOR FINDING CITY NEAR BY TOWM CITY https://www.travelmath.com/cities-near/Pateros,+WA
# twitter api start here
import tweepy
from textblob import TextBlob
asecret = '9VK7wy1q8zeWsmoeflxRmitru3Xj2mPJQ1QaBzCWllhJa'
akey = '984689745581064192-iMSQFTTXhGK5Aezz8OYInicZSlp51st'
csecret = 'EZsRWFVZ814qaVWfjlyKErAvATPu0wHE1kyoDNka8DiTafwaTM'
ckey = 'LJRTLQkwzAVroGDmVJOlsIQjb'
def twitter(twitloc,id):
    logger.info(f'Twitter Method : Retreving data from twitter api')
    Twitter.objects.all().delete()
    twit_data1 = Twitter.objects.filter(p_id=id)
    twit_data = twit_data1.count()
    if twit_data == 0:
        auth = tweepy.OAuthHandler(ckey,csecret)
        auth.set_access_token(akey,asecret)
        api = tweepy.API(auth)
        public_tweets = tweepy.Cursor(api.search, q=twitloc).items(10)
        for twit in public_tweets:
            twit_text = twit.text
            twit_count = twit.retweet_count
            twit_id = twit.id
            # twit_img = twit.__dict__['_json']['entities']['media'][0]['media_url']
            twit_img = twit.user.profile_image_url
            # twit_user1 = twit.__dict__['_json']['entities']['user_mentions'][0]['name']
            twit_date = twit.created_at
            twit_user2 = twit.user.name
            twit_like = twit.favorite_count
            dt = date.today()
            twit_insert = Twitter(p_id=id,twit_text=twit_text,dt=dt,twit_count=twit_count,twit_id=twit_id,twit_img=twit_img,twit_user2=twit_user2,twit_like=twit_like,twit_date=twit_date).save()

        twitter_data = Twitter.objects.filter(p_id=id)
    else:
        twitter_data = twit_data1
    logger.info(f'XXXXX----------Twitter Method End-----XXXXXXX')
    return twitter_data
#xxxxxxx-------end-------xxxxxxx

# XXXXXXXXXXX------------SEARCH DATA-----------XXXXXXXXXXXXXXX
def search(request,s):
    logger.info(f'Search Method : Retreving data for Search , Search Word : {s}')
    # search1 = Location_add.objects.filter(name__icontains=s)
    search = Usa_state_park_list.objects.filter(name__icontains=s,state='California')
    logger.info(f'XXXXX----------Search Method End-----XXXXXXX')
    return render(request,'search.html',{'search':search})

# XXXXXXXXXXX------------END SEARCH------------XXXXXXXXXXXXXXX

# XXXXXXXXXXX-----------DISTANCE FROM LAT,LONG------XXXXXXXX
def get_distance(lat1, lon1, lat2, lon2):
	R = 6373.0
	lat1 = radians(lat1)
	lon1 = radians(lon1)
	lat2 = radians(lat2)
	lon2 = radians(lon2)
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c
	return round(distance, 2)
# XXXXXXXXX-----------END---------------XXXXXXXXXXX



# XXXXXXXXXXX-----------START HOTEL SECTION--------XXXXXXXXXXXX
def park_hotel(request,p_id):
    logger.info(f'Park Hotel Method : Retreving hotel info using Tripadvisor API , for park id : {p_id}')
    # Park_hotel.objects.all().delete()
    p_id = int(p_id)
    location_single = Location_add.objects.filter(id=p_id)
    for loc in location_single:
        park_loc = loc.city
        park_state = loc.state
        logitude = loc.logitude
        latitude = loc.latitude
        park_country = loc.country
        park_nm = loc.name
        park_name =park_loc

    park_data1 = Park_hotel.objects.filter(p_id=p_id)
    park_data = park_data1.count()
    a = []
    if park_data == 0:
        url = "https://tripadvisor1.p.rapidapi.com/locations/search"
        querystring = {"location_id":"1","limit":"20","sort":"relevance","offset":"0","lang":"en_US","currency":"USD","units":"km","query":park_name}
        headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "6627e8d370mshd8cc18968140872p16f9c5jsnf6009960500f"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        park_json = response.text
        hoteldata = json.loads(park_json)['data']
        z = 0

        for i in hoteldata:
            m = hoteldata[z]['result_object']
            try:
                h_img = m['photo']['images']['large']['url']
                h_name = m['name']
                lat2 = m['latitude']
                lon2 = m['longitude']
                cat = m['category']['key']
            except KeyError:
                pass
            # Main Function
            km = get_distance(float(latitude),float(logitude),float(lat2),float(lon2))
            km = km/1.609344
            hotel_insert = Park_hotel(p_id=p_id,h_name=h_name,h_img=h_img,km=km,cat=cat).save()
            z = z+1


        hotel_data = Park_hotel.objects.filter(p_id=p_id).order_by('km')
    else:
        hotel_data = park_data1.order_by('km')
    logger.info(f'XXXXX----------Park Hotel Method End-----XXXXXXX')
    return render(request,'park_api_data.html',{'hotel_api':hotel_data})
# XXXXXXXXXXX----------END HOTEL SECTION-----------XXXXXXXXXXXX



# XXXXXXXXXXX-----------START BY CITY HOTEL SECTION--------XXXXXXXXXXXX
def park_city(city):
    # Park_hotel.objects.all().delete()
    logger.info(f'Park City Method : Retreving data for Park City using Tripadvisor API, City Name : {city}')
    park_city1 = Park_hotel_city.objects.filter(city=city)
    park_city = park_city1.count()
    a = []
    if park_city == 0:
        url = "https://tripadvisor1.p.rapidapi.com/locations/search"
        querystring = {"location_id":"1","limit":"20","sort":"relevance","offset":"0","lang":"en_US","currency":"USD","units":"km","query":city}
        headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "6627e8d370mshd8cc18968140872p16f9c5jsnf6009960500f"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        park_json = response.text
        hoteldata = json.loads(park_json)['data']
        z = 0

        for i in hoteldata:
            m = hoteldata[z]['result_object']
            try:
                h_img = m['photo']['images']['large']['url']
                h_name = m['name']
                cat = m['category']['key']
            except KeyError:
                pass
            # Main Function
            logger.info(f'Park City Method : Inserting data for park hotel city')
            hotel_insert = Park_hotel_city(h_name=h_name,h_img=h_img,cat=cat,city=city).save()
            z = z+1
        logger.info(f'Park City Method : Retreving data from Park hotel City ')
        hotel_city = Park_hotel_city.objects.filter(city=city)
    else:
        hotel_city = park_city1
    logger.info(f'XXXXX----------Park city Method End-----XXXXXXX')
    return hotel_city
# XXXXXXXXXXX----------END HOTEL BY CITY SECTION-----------XXXXXXXXXXXX

# XXXXXXXXXXX-----------START HOTEL super search SECTION--------XXXXXXXXXXXX
def park_hotel_search(request,p_id):
    hotel_data = park_city(p_id)
    return render(request,'park_api_data_search.html',{'hotel_api':hotel_data})
# XXXXXXXXXXX----------END HOTEL super search SECTION-----------XXXXXXXXXXXX


# XXXXX------Side bar load----XXXXXXX
def res_sidebar(request):
    return render(request,'res_sidebar.html')
# XXXXXX------END------XXXXXX
# login
def signin(request):
    logger.info(f'XXXXX----------SignIn Method Start-----XXXXXXX')
    if request.method=='POST':
        em=request.POST['em']
        ps=request.POST['ps']
        # send_mail('subject', 'tabish', 'tabishadnan9@gmail.com', ['tabishadnan8@gmail.com'])
        user = auth.authenticate(username=em,password=ps)
        if user is not None:
            auth.login(request, user)
            logger.info(f'SignIn Method : User Successfully  SignIn and enter to  Home Page User Id : {em}')
            return redirect('/')
        else:
            logger.info(f'SignIn Method : User Failed to SignIn because user name or password not Exits or not Matched')
            return render(request,'signin.html',{'msg':'User Name or Password Not Exits..!'})

    else:
        return render(request,'signin.html')
# end
# XXXXXXXXX---------SIGN-UP-------XXXXXXXXXXXX
def signup(request):
    logger.info(f'XXXXX----------SignUp Method Start-----XXXXXXX')
    if request.method == 'POST':
        nm = request.POST.get('nm')
        ps = request.POST.get('ps')
        em = request.POST.get('em')
        activity = request.POST.getlist('activity')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        otp = random.randint(0,9999)
        # activities convert into list
        a1 = []
        for ax in activity:
            aa1 = ast.literal_eval(ax)
            ad = int(aa1)
            a1.append(ad)
            # end

        # tabmail(em,otp)
        logger.info(f'SignUp Method : Checking OTP')
        insert = SignUp(name=nm,password=ps,email=em,activity=a1,city=city,state=state,country=country,otp=otp)
        insert.save()
        if User.objects.filter(username=em).exists():
            logger.info(f'SignUp Method : User Name  Exits')
            return render(request,'signup.html',{'msg':'User Name Exits..!'})
        else:
            user = User.objects.create_user(username=em,password=ps,email=em,first_name=nm,is_superuser=0)
            user.save()
            auth.login(request, user)
            logger.info(f'SignUp Method : Created new USER with user name : {em}')
            return render(request, 'home.html',{'msg':'Registered Successfully...'})

    activity = Activities.objects.all().order_by('-id')
    logger.info(f'XXXXX----------SignUp Method End-----XXXXXXX')
    return render(request, 'signup.html',{'activity_data':activity})


def logout1(request):
    # also need user id here
    logger.info(f'XXXXX----------Logout Method Start-----XXXXXXX')
    auth.logout(request)
    logger.info(f'XXXXX----------LogOUT Method End User Successfully logout-----XXXXXXX')
    return redirect('/')
# XXXXX------END------XXXXXX

# XXXX----IMAGE REVIEW----XXXXX
def img_review():
    logger.info(f'XXXXX----------Image review Method Start-----XXXXXXX')
    image1 = Imd_Review.objects.all()
    logger.info(f'XXXXX----------Image review Method End-----XXXXXXX')
    return  image1
# XXXX----END----XXXX

# wishlist function fetch
def wish_fetch():
    logger.info(f'XXXXX----------Wish List Fetch  Method Start-----XXXXXXX')
    wish_fetch1 = Wishlist.objects.all()
    logger.info(f'XXXXX----------Wish List Fetch  Method End-----XXXXXXX')
    return  wish_fetch1
# end
#XXXXX--------WEATHER------XXXXXXXXX
def cweather(request,city):
    logger.info(f'XXXXX----------Weather Method Start : fetching weather for city : {city}-----XXXXXXX')
    api_key = "0c60c309811553f3e83e6d5f66032080"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    y = x['main']
    a = x['wind']
    v = x['visibility']
    w = x['weather'][0]
    wther = (y,a,v,w)
    logger.info(f'XXXXX----------Weather Method End-----XXXXXXX')
    return render(request,'weather.html',{'wther':wther})

# XXXXXX-----END WEATHER------XXXXXXX

# XXXXXX------GOOGLE API FOR NEWS-----XXXXXXX
def google_news_api(request,park_city):
    logger.info(f'Google News API  Method Start : fetching news for location : {park_city}')
    googlenews = GoogleNews()
    googlenews = GoogleNews('en','d')
    googlenews.search(park_city)
    googlenews.getpage(1)
    a = googlenews.result()

    if not a:
        googlenews.search(park_city)
        googlenews.getpage(1)
        b = googlenews.result()
    else:
        b = a
    res_list = []
    for i in range(len(b)):
        if b[i] not in b[i + 1:]:
            res_list.append(b[i])
    z = len(res_list)
    logger.info(f'XXXXX----------Google News API Method End-----XXXXXXX')
    return render(request,'news_update.html',{'news_api':res_list,'l':a})
# XXXXXXX--------END-------XXXXXX

# XXXXXX------GOOGLE API FOR NEWS-----XXXXXXX
def google_news_api1(request,id):
    logger.info(f'Google News API 1 Method Start : fetching news for location Id : {id}')
    l_list = Usa_state_park_list.objects.all().filter(id=id)
    recomm_loc = Usa_park_list_ded.objects.all().filter(list_id=id)
    for rcl in recomm_loc:
        main_city = rcl.city
    for i in l_list:
        state = i.state
        park_name = i.name

    googlenews = GoogleNews()
    googlenews = GoogleNews('en','d')
    googlenews.search(park_name + state)
    googlenews.getpage(1)
    a = googlenews.result()

    if not a:
        googlenews.search(main_city)
        googlenews.getpage(1)
        b = googlenews.result()
    else:
        b = a
    res_list = []
    for i in range(len(b)):
        if b[i] not in b[i + 1:]:
            res_list.append(b[i])
    z = len(res_list)
    logger.info(f'XXXXX----------Google News API 1 Method End-----XXXXXXX')
    return render(request,'news_update.html',{'news_api':res_list,'l':a})
# XXXXXXX--------END-------XXXXXX


# XXXXXXX-------COUNTRY IP DATA ----XXXXX
def country_ip():
    with urllib.request.urlopen("https://ipinfo.io/json") as url:
        data = json.loads(url.read().decode())
        cnt = data['country']
        return cnt

#   xxxxx------end-----xxxxx

# XXXXXXXX-----------PARK SAFETY--------XXXXXXXXXXXXX
def park_safety():
    logger.info(f'XXXXX----------Park Safety Method Start-----XXXXXXX')
    safety = Safety_data.objects.all()
    logger.info(f'XXXXX----------Park Safety Method End-----XXXXXXX')
    return safety

# XXXXXXXXX----------END----------XXXXXXXXXXXX


# XXXXXXXX-----------corona state SAFETY--------XXXXXXXXXXXXX
def corona_safety(state):
    logger.info(f'Corona Safety Method Start  for state : {state}')
    corona_safety = Covid_state_link.objects.filter(usa_state=state)
    logger.info(f'XXXXX----------Corona Safety Method End-----XXXXXXX')
    return corona_safety

# XXXXXXXXX----------END----------XXXXXXXXXXXX

def home(request):
    '''here we write all docu for home'''
    # Park_hotel.objects.all().delete()

    logger.info(' Home Method : Retreving country_ip ')
    country_ip1 = country_ip()
    logger.info(' Home Method : Retreving country_ip ',country_ip1)
    # todo next line is to be commented
    logger.info(' Home Method : Retreving Guideline_detail ')
    IPAddr = socket.gethostbyname("google.com")
    logger.info(' Home Method : Retreving Park tag ')
    # get total time taken to execute the program for home
    logger.info(' Home Method : End of Home Section ')
# XXXXXXXXXX-----------NEAR BY SECTION--------XXXXXXXXXX
    return render(request,'home.html',{'country':country_ip1,'IPAddr':IPAddr})


def demo(request):
    '''demo method used  for testing home page in live server when product will live it will remove'''
    l_list = Usa_state_park_list.objects.all().filter(state='California',tag='State Forests')
    for i in l_list:
        state = i.state
        park_name = i.name
        imagelink = i.imagelinks
        tag = i.tag
        iid = i.id

        # camera image remove SECTION
        imagelink1 = imagelink.split(" ")
        image_replace = []
        replace_img1 = ['media/home/park_img/cali_state_park.png']
        RANGE = 5000
        for href1 in imagelink1:
            href = href1.strip("[").strip("'',]")
            req = requests.get(href, headers={'User-Agent': 'Mozilla5.0(Google spider)', 'Range': 'bytes=0-{}'.format(RANGE)})
            im = Image.open(BytesIO(req.content))
            width = im.size[1]
            if width != 80:
                image_replace.append(href)
                replace_img1.append(href)
            else:
                img3 = random.choice(replace_img1)
                image_replace.append(img3)
        Usa_state_park_list.objects.filter(id=iid).update(imagelinks=image_replace)
            # end


    return render(request,'demo.html')

# XXXXXX------END------XXXXXX

def nearby(request,lat,lon):
    logger.info(f'NearBy  Method Start User lat : {lat} , User Lon : {lon}')
    # XXXXXXXXXX-----------NEAR BY SECTION--------XXXXXXXXXX
    # g-map api : AIzaSyAiqlCyo-hqpavT5JRjZ-Rwr1KbG0NtIig
    # if request.method=='POST':
    #     lat = request.POST.get('lat')
    #     lon = request.POST.get('lon')
    near = Location_add.objects.all()
    city = []
    print('lon : ',lon,'lat :',lat)
    for n in near:
        lon2 = float(n.logitude)
        lat2 = float(n.latitude)
        km = get_distance(float(lat),float(lon),float(lat2),float(lon2))

        if km < 100:
            city.append(n.city)
            break

        # url2 = "https://maps.googleapis.com/maps/api/geocode/json?"
        # url2 += "latlng=%s,%s&sensor=false,&key=AIzaSyAiqlCyo-hqpavT5JRjZ-Rwr1KbG0NtIig" % (lat,lon)
        # v = urllib.request.urlopen(url2)
        # j = json.loads(v.read())
        # # components = j['results'][4]['address_components']
        # # state=components[3]['long_name']
    state=city[0]
    if len(city) !=0:
        live_data = park_city(state)
    else:
        live_data = near
    logger.info(' Home Method : End of Nearby Section ')
    return render(request,'nearyou.html',{'near':near,'state':state,'live_data':live_data})


    # XXXXXX------END------XXXXXX

# XXXXXXXXXXXXX-----START ACTIVITY DATA-----XXXXXXXXXXXX
def activity_data(request,aname,id):
    logger.info(f'Activity data  Method Start : activity name :  {aname} , activity Id : {id}')
    logger.info(' Activity data Method : Retreving Location_add')
    location = Location_add.objects.all()
    logger.info(' Activity data Method : Retreving Activities')
    activity1 = Activities.objects.values_list().filter(id=id)[0][2]
    logger.info(' Activity data Method : Retreving Park_activity')
    park_list_scrp = Park_activity.objects.values_list().filter(activity__icontains=aname)
    pls = []
    for pls1 in park_list_scrp:
        pls.append(pls1[1])
    logger.info(' Activity data Method : Retreving Location_bypublic added by user')
    location_user = Location_bypublic.objects.all().filter(status='unblock')
    lid = []
    lid1 = []
    for i in location:
        location_act = i.activity
        id1 = i.id
        location_activity = location_act.strip('][').split(', ')

        for a in location_activity:
            a = int(a)
            if a  == id:
                lid.append(id1)
    for i in location_user:
        location_act = i.activity
        id1 = i.id
        location_activity = location_act.strip('][').split(', ')

        for a in location_activity:
            a = int(a)
            if a  == id:
                lid1.append(id1)

    logger.info(' Activity data Method : Retreving Location_add for  state California')
    new_location = Location_add.objects.all().filter(pk__in=lid,state='California')
    new_location1 = Location_bypublic.objects.all().filter(pk__in=lid1,state='California')
    new_location2 = Usa_state_park_list.objects.all().filter(pk__in=pls,state='California')
    total_count = new_location.count() + new_location1.count() +new_location2.count()
    Activities.objects.filter(id=id).update(count=total_count)
    Search_data1 = Search_data.objects.all()
    country_ip1 = country_ip()
    logger.info(f'XXXXX----------activity_data Method End-----XXXXXXX')
    return render(request,'activity_data.html',{'location':new_location,'id':id,'country':country_ip1,'location1':new_location1,'location2':new_location2,'aname':aname})
# XXXXXX-----END ACTIVITY DATA-----XXXXXXX

# XXXXXXXXXXXXX-----START Facilities DATA-----XXXXXXXXXXXX
def facilities_data(request,aname,id):
    logger.info(f'Facilities data  Method Start : facility name :  {aname} , facility Id : {id}')
    logger.info(' Facility Method : Retreving Location_add')
    location = Location_add.objects.all()
    logger.info(' Facility Method : Retreving Facilities')
    facility = Facilities.objects.values_list().filter(id=id)[0][2]
    logger.info(' Facility Method : Retreving Park_activity')
    park_list_scrp = Park_activity.objects.values_list().filter(activity__icontains=aname)
    pls = []
    for pls1 in park_list_scrp:
        pls.append(pls1[1])
    lid = []
    for i in location:
        location_act = i.facility
        id1 = i.id
        location_activity = location_act.strip('][').split(', ')

        for a in location_activity:
            a = int(a)
            if a  == id:
                lid.append(id1)

    new_location = Location_add.objects.all().filter(pk__in=lid)
    new_location1 = Location_bypublic.objects.all().filter(pk__in=lid)
    new_location2 = Usa_state_park_list.objects.all().filter(pk__in=pls,state='California')
    total_count = new_location.count() + new_location1.count() +new_location2.count()
    Facilities.objects.filter(id=id).update(count=total_count)
    logger.info(f' Facility data Method : NO. of facility count {total_count}')
    wish_data = wish_fetch()
    country_ip1 = country_ip()
    logger.info(f'XXXXX----------Facility_data Method End-----XXXXXXX')
    return render(request,'activity_data.html',{'location':new_location,'wish_fetch':wish_data,'country':country_ip1,'location1':new_location1,'location2':new_location2})
# XXXXXX-----END Facilities DATA-----XXXXXXX

# XXXXXXXXXXXXXX-----START PARK DETAILS DATA-----XXXXXXXXXXXXXXX


def park_detail(request,id):
        logger.info(f'Park Detail Method : Retreving data for park detail for  , park id : {id}')
        logger.info(' Park Detail Method : Retreving Location_add')
        location_single = Location_add.objects.filter(id=id)

        for cat_id in location_single:
            location_cat = cat_id.category
            location_category = location_cat.strip('][').split(', ')

            location_fat = cat_id.facility
            location_facility = location_fat.strip('][').split(', ')

            location_act = cat_id.activity
            location_activity = location_act.strip('][').split(', ')
            location_city = cat_id.city
            park_name = cat_id.name
            logitude = cat_id.logitude
            latitude = cat_id.latitude
            location_state = cat_id.state

        cat_l = []
        fat_l = []
        act_l = []

        #XXX---getting category filter data---XXX
        for cx in location_category:
            ca1 = ast.literal_eval(cx)
            cd = int(ca1)
            cat_l.append(cd)
        cat_data = Categories.objects.all().filter(pk__in=cat_l)
        # XXX----END-----XXXX

        #XXX---getting facility filter data---XXX
        for fx in location_facility:
            fa1 = ast.literal_eval(fx)
            fd = int(fa1)
            fat_l.append(fd)
        fat_data = Facilities.objects.all().filter(pk__in=fat_l)
        # XXX----END-----XXXX

        #XXX---getting Activities filter data---XXX
        for ax in location_activity:
            aa1 = ast.literal_eval(ax)
            ad = int(aa1)
            act_l.append(ad)
        act_data = Activities.objects.all().filter(pk__in=act_l)
        # XXX----END-----XXXX

        #XXXXXXX-------Recommended section start--------XXXXXXXXX
        location = Location_add.objects.all()
        lid = []
        for i in location:
            location_act = i.activity
            id1 = i.id
            location_activity = location_act.strip('][').split(', ')

            for a in location_activity:
                a = int(a)
                if a  == act_l[0]:
                    lid.append(id1)

        recomm_loc = Location_add.objects.all().filter(pk__in=lid)
        # XXXXXXXX--------END-------XXXXX
        logger.info(' Park Detail Method : Retreving Review')
        review = Review.objects.all().filter(park_tag='local',park_id=id).order_by('-id')[:3]
        logger.info(' Park Detail Method : Retreving Review image')
        image = img_review()
        logger.info(' Park Detail Method : Retreving Review count')
        review_count = Review.objects.filter(park_id=id).count()

        #xxxxx------trending section------xxxxx
        trend_insert(id,'home')
        #xxxxx-----end-----xxxxx
        # XXXX----WEATHER----XXXXXX
        # wther = cweather(location_city)
        # XXXXX-----END-----XXXXXX

        # xxxx------twitter api----xxxxxxx
        logger.info(' Park Detail Method : Retreving Twitter api for park details')
        try:
            twit_api = twitter(park_name,id)
        except:
            twit_api =''


        # xxxxxx-------end------xxxxxx

        # XXXXXXXX--------SEARCH DATA INSERT-------XXXXXXXXXXX
        u = request.user.is_authenticated
        if u:
            user = User.objects.get(username=request.user.username)
            Search_data(user=user,p_id=id,loc=location_city).save()
            # logger.info('reteiving park info for user',request.user.username)
        # XXXXXXXXX---------END----------XXXXXXXXXX
        random1 = random.randint(1,5)
        logger.info(' Park Detail Method : Retreving park_safety for park details')
        safety = park_safety()
        logger.info(' Park Detail Method : Retreving corona_safety for park details')
        c_safety = corona_safety(location_state)
        logger.info(f'XXXXX----------Park Detail Method End-----XXXXXXX')
        return render(request,'park_detail.html',{'location_single':location_single,'cat_id':cat_data,'fat_id':fat_data,'act_id':act_data,'id':id,'review':review,'tag':'local','image':image,'r_cnt':review_count,'recomm_loc':recomm_loc,'random':random1,'twit_api':twit_api,'safety':safety,'c_safety':c_safety})

# XXXXXX-----END PARK DETAILS DATA-----XXXXXXX

# XXXXXXXX-------USA ALL PARK-------XXXXXXXXXXXX
def usa_all_park(request):
    us_state = Usa_state.objects.all()

    return render(request,'usa_all_park.html',{'state_name':us_state})

# XXXX-----END----XXXXX

# XXXXXXXX-------USA state_park PARK-------XXXXXXXXXXXX
def state_park(request,id):
    # Usa_state_park_list.objects.filter(state=id).delete()
    near = Location_add.objects.all()
    data = Usa_state_park_list.objects.all().filter(state=id)
    return render(request,'state_park_list.html',{'near':near,'state':id,'data':data})

# XXXX-----END----XXXXX

def message(request):
    return render(request, 'message.html')


def faq(request):
    logger.info(f'FAQ Method : Retreving data for faq')
    Review_filter.objects.all().delete()
    # for row in Usa_state_park_list.objects.all().reverse():
    #     if Usa_state_park_list.objects.filter(name=row.name).count() > 1:
    #         row.delete()
    logger.info(f'XXXXX----------FAQ Method End-----XXXXXXX')
    return render(request, 'faq.html')

def covid(request):
    logger.info(f'covid Method : Retreving data for faq')
    logger.info(f'XXXXX----------COVID Method End-----XXXXXXX')
    return render(request, 'covid.html')

def virtual(request,id):
    logger.info(f'Virtual Method : Retreving data for virtual park , park id : {id}')
    data = Virtual.objects.all().filter(id=id)
    logger.info(f'XXXXX----------Virtual Method End-----XXXXXXX')
    return render(request, 'virtualdata.html',{'data':data})

def virtual_list(request):
    virtual = Virtual.objects.all()
    return render(request,'virtual_list1.html',{'virtual':virtual})

# XXXXXX--------US NATIONAL STATE-----XXXXXXX
def us_national_park(request,id):
    if id == 'state':
        us_state = Usa_state.objects.all()
        return render(request,'us_national_park.html',{'state_name':us_state})
    else:
        return render(request,'us_alphabet.html')


def us_national_state(request,id):
    us_state = Usa_state.objects.filter(id=id)
    for u in us_state:
        url1 = u.api_url
        s_name = u.name

    r = requests.get(url1)
    data = r.json()

    return render(request,'us_national_state.html',{'state_name':data['data'],'s_name':s_name})

def us_national_details(request,id):
    r = requests.get(f'https://mychaps.net/us-state-single-api/{id}')
    data1 = r.json()
    data = data1['data']

    #XXXXXX--------Reccommend section start here-------XXXXXX
    act_data = Activities.objects.all()
    activity_id_list = []
    park_name = []
    location_city = []
    for d in data:
        park_name.append(d['fullName'])
        location_city.append(d['addresses'][1]['city'])
        for z in d['activities']:
            nps_activity = z['name']
            for main_activity in act_data:
                main_activity1 = main_activity.name
                hist = main_activity.history
                if main_activity1.lower() == nps_activity.lower():
                    activity_id_list.append(hist)

    #XXXXXXX-------Recommended section start--------XXXXXXXXX

    recomm_loc = Location_add.objects.all().filter(city=location_city[0])
    # XXXXXXXX--------END-------XXXXX

    review = Review.objects.all().filter(park_tag='nsp',park_id=id)
    image = img_review()
    review_count = Review.objects.filter(park_id=id).count()
    #xxxxx------trending section------xxxxx
    trend_insert(id,'nsp')
    #xxxxx-----end-----xxxxx

    return render(request,'us_national_details.html',{'state_name':data,'id':id,'tag':'nsp','review':review,'image':image,'r_cnt':review_count,'recomm_loc':recomm_loc})

def us_national_alpha(request,id):
    r = requests.get(f'https://mychaps.net/us-state-alphabet-api/{id}')
    data1 = r.json()
    data = data1['data']
    return render(request,'us_national_state.html',{'state_name':data})

# XXXXXX------END------XXXXXXX

# XXXXXXXXXXXXX--------COUNTRY WISE------XXXXXXXXXX
def by_country(request):
    return render(request,'by_country.html')

def country_alphabet_in(request):
    return render(request,'country_alphabet_in.html')


# XXXXXXXXXX-------END-------XXXXXXXX

# XXXXXXXXXX----------review---------XXXXXXXXXXXX
def review(request):
    if request.method == 'POST':
        overall = int(request.POST.get('overall',1))
        behav = int(request.POST.get('behaviour',1))
        service = int(request.POST.get('service',1))
        comt = request.POST.get('comt')
        img = request.FILES.getlist('img')
        id = request.POST.get('id')
        tag = request.POST.get('tag')
        user_id = request.POST.get('user_id')
        # user_nm = request.POST.get('user_nm')
        p_date = datetime.date.today()
        if user_id == 'tabishadnan9@gmail.com':
            name_list = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth',
                 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Thomas', 'Sarah', 'Charles', 'Karen',
                 'Christopher', 'Nancy', 'Daniel', 'Lisa', 'Matthew', 'Margaret', 'Anthony', 'Betty', 'Donald', 'Sandra',
                 'Mark', 'Ashley', 'Paul', 'Dorothy', 'Steven', ' Kimberly', 'Andrew', 'Emily', 'Kenneth','Donna','Joshua',
                 'Michelle','Kevin','Carol','Brian','Amanda','George','Melissa','Edward','Deborah','Ronald','Stephanie',
                 'Timothy','Rebecca','Jason','Laura','Jeffrey','Sharon','Ryan','Cynthia','Jacob','Kathleen','Gary','Amy',
                 'Nicholas','Shirley','Eric','Angela','Jonathan','Helen','Madison','Isabella','Olivia','Lily']
            user_nm = random.choice(name_list)
        else:
            user_nm = request.POST.get('user_nm')
        insert = Review(user_id=user_id,park_id=id,park_tag=tag,overall=overall,service=service,behaviour=behav,comment=comt,p_date=p_date,user_nm=user_nm)
        insert.save()
        rid = insert.id
        for f in img:
            photo = Imd_Review(rid=int(rid), img=f)
            photo.save()

        return redirect(f'after_review/{tag},{id}')

        # if tag == 'old':
        #     return redirect(f'nearby-data/{id}',{'msg':'inserted Successfully'})
        # elif tag == 'nsp':
        #     return redirect(f'us_national_details/{id}',{'msg':'inserted Successfully'})
        # else:
        #     return redirect(f'park-detail/{id}')


    else:
        return render(request, 'home.html')

def after_review(request,tag,id):
    if tag == 'nsp':
        id = str(id)
    else:
        id = int(id)
    review = Review.objects.all().filter(park_tag=tag,park_id=id).order_by('-id')
    image = img_review()
    review_count = Review.objects.filter(park_id=id).count()
    return render(request, 'after_review.html',{'review':review,'image':image,'review_count':review_count,'tag':tag,'id':id,'user_back':'user_back'})

# def after_review(request,tag,id):
#     from .usa_models import state_review
#     state = state_review(tag)
#     sreview = state.objects.all().filter(pid=id)
#     return render(request, 'after_review.html',{'tag':tag,'id':id,'sreview':sreview,'user_back':'user_back'})

def load_review(request):
    logger.info(f'Load Review Method : Retreving review using pagination')
    if request.method == 'POST':
        limit = int(request.POST.get('limit'))
        start = int(request.POST.get('start'))
        tag = request.POST.get('state')
        id = request.POST.get('id')
        state = state_review(tag)
        pnm = Usa_state_park_list.objects.get(id=id)
        name = pnm.name
        sreview = Alaska.objects.all().filter(pid=id)
        paginator = Paginator(sreview,2)
        page = start
        p = paginator.page(page)
        time.sleep(2)

        p_count = p.__len__()
        if p_count == 0:
            return  HttpResponse("")
        else:
            logger.info(f'XXXXX----------Load Review Method End-----XXXXXXX')
            return render(request, 'sreview.html',{'tag':tag,'id':id,'sreview':p,'user_back':'user_back','name':name})



# XXXXXXXX--------END-------XXXXXXXXXX

# XXXXXXXXXXXXX--------Feedback-------XXXXXXXXXXXXX
def feedback(request):
    logger.info(f'Feedback Method : start feedback section  ')
    if request.method == 'POST':
        nm = request.POST.get('nm')
        em = request.POST.get('em')
        feed =request.POST.get('feed')
        p_date = datetime.date.today()
        logger.info(f'Feedback Method : Inserting feedback by User : {nm}')
        Feedback(nm=nm,em=em,feed=feed,p_date=p_date).save()
    logger.info(f'XXXXX----------Feedback Method End-----XXXXXXX')
    return render(request, 'feedback.html')
# XXXX-----END-----XXXXXX

# XXXXXXXX--------WISHLIST-------XXXXXXXXXXXX
def wishlist(request):
    logger.info(f'WishList Method : start wishlist section  ')
    if request.method == 'POST':
        id = request.POST.get('id')
        tag = request.POST.get('tag')
        user = request.POST.get('user')
        logger.info(f'WishList Method : inserting wishlist by user : {user} for park id : {id} ')
        Wishlist(p_id=id,tag=tag,u_id=user).save()
    logger.info(f'XXXXX----------WishList Method End-----XXXXXXX')
    return render(request, 'feedback.html')

def save_park(request):
    logger.info(f'save park Method : start save park section  ')
    user = User.objects.get(username=request.user.username)
    w_list = []
    a = []
    wish_data = Wishlist.objects.all().filter(u_id=user)
    for w in wish_data:
        if w.tag == 'old':
            aa = w.p_id
            a.append(aa)
        w_list.append(w.p_id)
    new_location = Location_add.objects.all().filter(pk__in=w_list)
    new_location1 = Location_bypublic.objects.all().filter(pk__in=w_list)
    new_location2 = Usa_state_park_list.objects.all().filter(pk__in=w_list)
    logger.info(f'XXXXX----------Save Park Method End-----XXXXXXX')
    return render(request,'save_park.html',{'location':new_location,'api_id':a,'location2':new_location2,'location1':new_location1})

def wishlist_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        tag = request.POST.get('tag')
        user = request.POST.get('user')
        logger.info(f'WishList Delete Method : Delete wishlist by user : {user} for park id : {id} ')
        Wishlist.objects.all().filter(p_id=id,u_id=user).delete()
        return render(request,'save_park.html')
    logger.info(f'XXXXX----------WishList Delete Method End-----XXXXXXX')
    return render(request,'wish_detail.html')

# wish detail here
def wish_detail(request,id):
    logger.info(f'WishList Detail Method : Start ')
    user = User.objects.get(username=request.user.username)
    wish_data = Wishlist.objects.all().filter(u_id=user,p_id=id).count()
    logger.info(f'WishList Detail Method : End ')
    return render(request,'wish_detail.html',{'wish_data':wish_data,'id':id,'z':wish_data})

def wish_detail1(request,id):
    logger.info(f'WishList1 Detail Method : Start ')
    user = User.objects.get(username=request.user.username)
    wish_data = Wishlist.objects.all().filter(u_id=user,p_id=id).count()
    logger.info(f'WishList1 Detail Method : End ')
    return render(request,'wish_detail1.html',{'wish_data':wish_data,'id':id,'z':wish_data})

# end
# XXXXXXXXXX----------Trending-------XXXXXXXXX
def trending(request):
    logger.info(f'Trending  Method : Start ')
    trend = Trending.objects.all().filter(qnt__gte=10)
    hm_list = []
    old_list = []
    nsp_list = []
    scraping_list = []

    for w in trend:
        if w.tag == 'home':
            a1 = w.p_id
            hm_list.append(a1)
        elif w.tag == 'scraping':
            a2 = w.p_id
            scraping_list.append(a2)
        else:
            a3 = w.p_id
            nsp_list.append(a3)

    new_location = Location_add.objects.all().filter(pk__in=hm_list)[:10]
    data = Usa_state_park_list.objects.all().filter(pk__in=scraping_list)[:10]
    logger.info(f'Trending  Method : End ')
    return render(request,'most_view.html',{'location':new_location,'api_id':old_list,'data':data})

def trend_insert(pid,tag):
    p_date = datetime.date.today()
    trend = Trending.objects.filter(p_id=pid,tag=tag)
    if trend.count() == 0:
        insert = Trending(p_id=pid,tag=tag,dt=p_date,qnt=1).save()
    else:
        for t in trend:
            q = t.qnt
            q = q+1
            update = Trending.objects.filter(p_id=pid,tag=tag).update(qnt=q)
#XXXX------END------XXXXXXX

# XXXXXXX--------GOOGLE NEWS-------XXXXXXXXXX
def google_news(request):
    return render(request,'google_news.html')
# XXXXXXXX-------END-------XXXXXXXX

# XXXXXXX--------nav cache -------XXXXXXXXXX
def nav(request):
    return render(request,'navbar_cache.html')
# XXXXXXXX-------END-------XXXXXXXX

# XXXXXXX--------nav cache -------XXXXXXXXXX
def reviewcache(request):
    return render(request,'review.html')
# XXXXXXXX-------END-------XXXXXXXX

# XXXXXXX--------nearby click  -------XXXXXXXXXX
def nearclick(request):
    return render(request,'nearby_click.html')
# XXXXXXXX-------END-------XXXXXXXX


# XXXXXXX--------delete_hotel click  -------XXXXXXXXXX
def hotel_delete_api(request):
    Park_hotel.objects.all().delete()
    return  HttpResponse("<h1>hotel db deleted</h1>")
# XXXXXXXX-------END-------XXXXXXXX

# XXXXXXXXXXX----------INSERTING SCRAPING DATA---------XXXXXXXXXXXX
def insert_scraping(request):
    # url = "https://www.stateparks.com/alaska_parks_and_recreation_destinations.html"
    r = requests.get(url)
    htmlcontent = r.content
    soup  = BeautifulSoup(htmlcontent, 'html.parser')

    park_name = soup.find_all('div',  id="parklink")
    #XXXXXX------ image scaping start----XXXXXX
    Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
    u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    }


    def download_images(name):
        data = name
        num_images = 20
        search_url = f"https://www.bing.com/images/search?q={data}&form=HDRSC2&first=1&tsc=ImageBasicHover"
        response = requests.get(search_url, headers=u_agnt)
        html = response.text
        b_soup = BeautifulSoup(html, 'html.parser')
        results = b_soup.findAll('div', {'class': 'img_cont hoff'})
        count = 0
        imagelinks = []
        for res in results:
            try:
                link1 = res.findAll('img')
                for i in link1:
                    link=i['data-src'].split('?')[0]
                    imagelinks.append(link)
                    count = count + 1
                if (count >= num_images):
                    break

            except KeyError:
                continue

        return imagelinks
    # XXXXXXX--------END-------XXXXXX


    n = 1
    for i in park_name:
        a = i.find("a", href=True)

        if n<111:
            tag = 'State Parks'
            link = a['href']
            name = i.text

            # image inserting
            img=download_images(name)

            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n >110 and n<120:
            tag ='State Recreation Areas'
            link = a['href']
            name = i.text
            img=download_images(name)

            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 119 and n < 126:
            tag = 'State Forests'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 125 and n < 131:
            tag = 'State Historic Sites'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 130 and n < 136:
            tag = 'State Fish Hatcherys'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 135 and n < 137:
            tag = 'State Nature Preserve'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 136 and n < 147:
            tag = 'State Reserves'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 146 and n < 157:
            tag = 'State Wildlife Areas'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 156 and n < 165:
            tag = 'National Parks'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 164 and n < 184:
            tag = 'National Forests'

            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 183 and n < 187:
            tag = 'National Historic Sites'

            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 186 and n < 218:
            tag = 'National Wildlife Refuges'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 217 and n < 221:
            tag = 'National Recreation Areas'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 220 and n < 222:
            tag = 'National Seashore'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()
        elif n > 221 and n < 223:
            tag = 'Metro and City Parks'
            link = a['href']
            name = i.text
            img=download_images(name)
            scrap_insert = Usa_state_park_list(name=name,link=link,tag=tag,state='Alaska',imagelinks=img).save()

        n = n+1


    return HttpResponse("<h1>Data Inserted Successfully....</h1>")

# XXXXXXXXXXXXX-------END---------XXXXXXXXX

# XXXXXXXXXXXXX---------insert_scraping_des---------XXXXXXXXXXX
def insert_scraping_des(request):
    data = Usa_state_park_list.objects.all().filter(state='Arkansas')
    for d in data:
        id = d.id
        link = d.link
        # print('here is link :',link)
        url = f"https://www.stateparks.com/{link}"
        r = requests.get(url)
        htmlcontent = r.content
        soup  = BeautifulSoup(htmlcontent, 'html.parser')
        park_des = soup.find('div',  class_="psbod").text
        address = soup.find('div',  class_="parkinfo").text
        direction = soup.findAll('div',  class_="psbod")[-1].text
        nearby = soup.findAll('div',  id="nearbyparklink")
        nearall = {}
        for i in nearby:
            des = i.text
            a = i.find("a", href=True)
            nearall[des] = a['href']

        data_insert = Usa_park_list_ded(list_id=id,country="USA",address=address,overview=park_des,direction=direction,nearby=nearall)
        data_insert.save()
    return HttpResponse("<h1>Data Inserted Successfully....</h1>")
# XXXXXXXXX------------END-----------XXXXXXXXX


# XXXXXXXXXXXXXX-----scraping PARK DETAILS DATA-----XXXXXXXXXXXXXXX
def scraping_park_detail(request,park_name,id):
        l_list = Usa_state_park_list.objects.all()
        loc_list = l_list.filter(id=id)
        recomm_loc = Usa_park_list_ded.objects.all().filter(list_id=id)
        for rcl in recomm_loc:
            main_city = rcl.city
        for i in loc_list:
            state = i.state
            park_name = i.name
            imagelink = i.imagelinks
            tag = i.tag
            iid = i.id

        # camera image remove SECTION
        imagelink1 = imagelink.split(" ")
        image_replace = []
        RANGE = 5000
        for href1 in imagelink1:
            href = href1.strip("[").strip("'',]")
            req = requests.get(href, headers={'User-Agent': 'Mozilla5.0(Google spider)', 'Range': 'bytes=0-{}'.format(RANGE)})
            im = Image.open(BytesIO(req.content))
            width = im.size[1]
            if width != 80:
                image_replace.append(href)
            else:
                image_replace.append('https://tse4.mm.bing.net/th/id/OIP.di33zDofkyDDB9V6psR5rAHaFj')
        # end

        park_city = Usa_park_list_ded.objects.get(list_id=id)
        try:
            city = park_city.city.replace(" ","+")
            # city = park_city.address.lower().split(park_name.lower())[-1].split('\n')[0].replace("\xa0\xa0\xa0", " ").split(f', {state.lower()}')[0].replace(' ','+').split('+')[-1].split('-')[-1]
            # if city=='':
            #     city = park_name.replace(" ","+")
            #
            # city = ''.join([i for i in city if not i.isdigit()])
            # l1 = []
            # l2 = sum(map(str.isupper, city))
            # if l2>1:
            #     for z in city:
            #         if z.isupper() == True:
            #             l1.append(z)
            #             c = city.split(l1[-1])[-1]
            #             city = l1[-1]+c
        except:
            city = park_city.city.replace(' ','+')

        try:
            neartown = park_city.neartown.strip('][').split(', ')[0].split("'")[1].replace(' ','+')
        except:
            neartown = 'nonedisplaytab'
        alltown = park_city.neartown.strip('][').split(', ')
        # XXXXXXXX--------END-------XXXXX
        recom_park = l_list.filter(~Q(id=id),state=state,tag=tag)[:10]
        review = Review.objects.all().filter(park_tag='local',park_id=id).order_by('-id')[:3]
        activity_park = Park_activity.objects.all().filter(park_id=id).order_by('-id')
        im = []
        for ap in activity_park:
            im.append(ap.activity)
        img_act = Img_activity.objects.all().filter(activity__in=im)
        image = img_review()
        review_count = Review.objects.filter(park_id=id).count()
        #xxxxx------trending section------xxxxx
        trend_insert(id,'scraping')
        #xxxxx-----end-----xxxxx
        # xxxx------twitter api----xxxxxxx
        twit_api = twitter(park_name,id)
        if not twit_api:
            try:
                twit_api = twitter(main_city,id)
            except:
                pass






        # xxxxxx-------end------xxxxxx
        # XXXXXXXX--------SEARCH DATA INSERT-------XXXXXXXXXXX
        u = request.user.is_authenticated
        # if u:
        #     user = User.objects.get(username=request.user.username)
        #     Search_data(user=user,p_id=id,loc=location_city).save()
        # XXXXXXXXX---------END----------XXXXXXXXXX
        random1 = random.randint(1,5)
        safety = park_safety()
        c_safety = corona_safety(state)
        try:
            wiki = wikipedia.summary(park_name)
        except:
            wiki = 'none113'
        gal_count = [9,10,11,12,13,14,15,16,17,18,19,1,2,3,4,5,6,7,8]
        return render(request,'collect_park_detail.html',{'location_single':recomm_loc,'id':id,'review':review,'image':image,'r_cnt':review_count,'recomm_loc':recomm_loc,'random':random1,'twit_api':twit_api,'safety':safety,'c_safety':c_safety,'state':state,'park_name':park_name,'imagelink':image_replace,'l_list':l_list,'recom_park':recom_park,'gal_count':gal_count,'city':city,'neartown':neartown,'alltown':alltown,'activity_park':activity_park,'img_act':img_act,'wiki':wiki,'tag':tag})

# XXXXXX-----END PARK DETAILS DATA-----XXXXXXX

# XXXXXXX---------City Name Update-------XXXXXXXXX
def usa_city_update(request,ct):
    park_list = Usa_state_park_list.objects.all().filter(state=ct).values_list('id', flat=True)
    # print('park list here : ',park_list)
    park_data = Usa_park_list_ded.objects.all().filter(list_id__in=park_list)

    for p in park_data:
        ass = p.address.lower()
        name = Usa_state_park_list.objects.get(id=p.list_id)
        pnm = name.name.lower()
        state = name.state.lower()
        park_city = p.city.replace(" ","+")
        try:
            # b = ass.split(pnm)[-1].split('\n')[0].replace("\xa0\xa0\xa0", " ").replace(',','').replace(' ','+')
            b = ass.lower().split(pnm)[-1].split('\n')[0].replace("\xa0\xa0\xa0", " ").split(f', {state}')[0].replace(' ','+').split('+')[-1]
            if b=='':
                b = pnm.replace(" ","+")
            b = ''.join([i for i in b if not i.isdigit()])
        except:
            b = ass.split(pnm)[-1]

        id = p.id
        city2 = b.replace("+"," ")

        url = f"https://www.travelmath.com/cities-near/{park_city}+{state}"
        r = requests.get(url)

        htmlcontent = r.content

        soup  = BeautifulSoup(htmlcontent, 'html.parser')
        park_name = soup.find_all('div', class_='boxbottom6')

        city = []
        for c in park_name:
            print('c is here:',c)
            a = c.findAll("a", href=True)
            print('a is here:',a)
            for i in a:
                print('hi tab : ',i)
                city.append(i.text.split(", ")[0])
        Usa_park_list_ded.objects.filter(id=id).update(neartown=city[:5])
        # print(city[:5])
    return HttpResponse(ct,'<br>')
# XXXXXXXX----------END---------XXXXXXXX

def sreview(request):
    Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
    u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    }
    def download_images(name):
        data = name
        num_images = 20
        search_url  = Google_Image + 'q=' + data
        response = requests.get(search_url, headers=u_agnt)
        html = response.text
        b_soup = BeautifulSoup(html, 'html.parser')
        results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
        count = 0
        imagelinks = []
        for res in results:
            try:
                link = res['data-src']
                imagelinks.append(link)
                count = count + 1
                if (count >= num_images):
                    break

            except KeyError:
                continue

        return imagelinks
    def get_place_details(fields,pid):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': pid,
            'fields': ",".join(fields),
            'key': 'AIzaSyDz3g9tfDY7PNX2aTWgjCwxYOTG6Hawk6A'
        }
        res = requests.get(endpoint_url, params=params)
        place_details = json.loads(res.content)
        return place_details
    def user_name():
        name_list = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 'William', 'Elizabeth',
                     'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 'Thomas', 'Sarah', 'Charles', 'Karen',
                     'Christopher', 'Nancy', 'Daniel', 'Lisa', 'Matthew', 'Margaret', 'Anthony', 'Betty', 'Donald',
                     'Sandra',
                     'Mark', 'Ashley', 'Paul', 'Dorothy', 'Steven', ' Kimberly', 'Andrew', 'Emily', 'Kenneth', 'Donna',
                     'Joshua',
                     'Michelle', 'Kevin', 'Carol', 'Brian', 'Amanda', 'George', 'Melissa', 'Edward', 'Deborah', 'Ronald',
                     'Stephanie',
                     'Timothy', 'Rebecca', 'Jason', 'Laura', 'Jeffrey', 'Sharon', 'Ryan', 'Cynthia', 'Jacob', 'Kathleen',
                     'Gary', 'Amy',
                     'Nicholas', 'Shirley', 'Eric', 'Angela', 'Jonathan', 'Helen', 'Madison', 'Isabella', 'Olivia', 'Lily']
        dt = ['2021-02-10','2021-02-11','2021-02-11','2021-01-19','2021-01-11','2020-09-21','2021-01-13','2021-02-14','2020-12-12','2020-11-29','2021-02-22']
        user_nm = random.choice(name_list)
        dt1 = random.choice(dt)
        return user_nm,dt1

    gmaps = googlemaps.Client(key='AIzaSyDz3g9tfDY7PNX2aTWgjCwxYOTG6Hawk6A')
    place_name = Usa_state_park_list.objects.all().filter(state='Arkansas')
    for p in place_name:
        pnm = p.name
        park_id = p.id
        state = p.state
        tag = p.tag
        places_result = gmaps.places(pnm)
        img = download_images(pnm)
        fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']
        pid = places_result['results'][0]['place_id']
        r = get_place_details(fields, pid)['result']['reviews']

        n = 4
        c = 0
        print('id : ',park_id)
        for i in r:
            name = user_name()
            img1 = img[c:n]
            user_nm = name[0]
            p_date = name[1]
            comment = i['text']
            rating = i['rating']

            insert = Sreview(pid=park_id,tag=tag,state=state,overall=rating,service=rating,behaviour=rating,comment=comment,user_nm=user_nm,img=img1,p_date=p_date).save()

            n = n+4
            c = c+4
    # Sreview.objects.all().delete()
    return HttpResponse('Data inserted Successfully....!')

# XXXXXXXXXXXXXX-----------END REVIEW--------XXXXXXXXXXXXXXX


def update_city(request,nm):
    def reverseGeocode(coordinates):
        result = rg.search(coordinates)
        return result

    gmaps = googlemaps.Client(key='AIzaSyDz3g9tfDY7PNX2aTWgjCwxYOTG6Hawk6A')
    place_name = Usa_state_park_list.objects.all().filter(state=nm)
    for p in place_name:
        pnm = p.name + nm
        park_id = p.id
        places_result = gmaps.places(pnm)
        lat = places_result['results'][0]['geometry']['location']['lat']
        lng = places_result['results'][0]['geometry']['location']['lng']
        a = reverseGeocode((lat, lng))
        tuple_list = dict(a[0].items())
        city_name = tuple_list['name']

        Usa_park_list_ded.objects.filter(list_id=park_id).update(city=city_name,lat=lat,lon=lng)
    return HttpResponse('Data inserted Successfully....!')

def addlocation(request):
    if request.method == 'POST':
        name = request.POST.get('name','name_empty')
        user_name = request.POST.get('user_name','name_empty')
        city = request.POST.get('city','city_empty')
        state = request.POST.get('state','state_empty')
        country = request.POST.get('country','country_empty')
        zipcode = request.POST.get('zipcode','zipcode_empty')
        address = request.POST.get('address','address_empty')
        logitude = request.POST.get('longitude','logitude_empty')
        latitude = request.POST.get('latitude','latitude_empty')
        overview = request.POST.get('overview','name_empty')
        categories = request.POST.getlist('category','category_empty')
        facilities = request.POST.getlist('facility','facility_empty')
        activities = request.POST.getlist('activity','activity_empty')
        img = request.FILES.getlist('img')

        # category convert into list
        c1 = []
        for cx in categories:
            ca1 = ast.literal_eval(cx)
            cd = int(ca1)
            c1.append(cd)
            # end
        # activities convert into list
        a1 = []
        for ax in activities:
            aa1 = ast.literal_eval(ax)
            ad = int(aa1)
            a1.append(ad)
            # end

        # facilities convert into list
        f1 = []
        for fx in facilities:
            fa1 = ast.literal_eval(fx)
            fd = int(fa1)
            f1.append(fd)
            # end
        for fi in img:
            fimg = fi
        insert = Location_bypublic(park_name=name,user_name=user_name,city=city,state=state,country=country,zipcode=zipcode,address=address,logitude=logitude,
        latitude=latitude,overview=overview,category=c1,facility=f1,activity=a1,img=fimg)
        insert.save()
        rid = insert.id
        for f in img:
            photo = Img_bypublic(location_bypublic_id=rid,img=f)
            photo.save()
        return render(request,'location_public.html',{'msg':'Added Successfully..! wait for admin approval'})
    else:
        # Location_bypublic.objects.all().delete()

        category = Categories.objects.all()
        activity = Activities.objects.all()
        facility = Facilities.objects.all()
        return render(request,'location_public.html',{'category_data':category,'activity':activity,'facility':facility})

# XXXXXXXXXX------------END---------XXXXXXXXXXXXX


# XXXXXXXXXXXXXX-----START PARK DETAILS DATA-----XXXXXXXXXXXXXXX
def park_detail_user(request,id):
        logger.info(f'park_detail_user  Method : Retreving park detail added by user ')
        location_single = Location_bypublic.objects.filter(id=id)

        for cat_id in location_single:
            location_cat = cat_id.category
            location_category = location_cat.strip('][').split(', ')

            location_fat = cat_id.facility
            location_facility = location_fat.strip('][').split(', ')

            location_act = cat_id.activity
            location_activity = location_act.strip('][').split(', ')
            location_city = cat_id.city
            park_name = cat_id.park_name
            logitude = cat_id.logitude
            latitude = cat_id.latitude
            location_state = cat_id.state

        cat_l = []
        fat_l = []
        act_l = []

        #XXX---getting category filter data---XXX
        for cx in location_category:
            ca1 = ast.literal_eval(cx)
            cd = int(ca1)
            cat_l.append(cd)
        cat_data = Categories.objects.all().filter(pk__in=cat_l)
        # XXX----END-----XXXX

        #XXX---getting facility filter data---XXX
        for fx in location_facility:
            fa1 = ast.literal_eval(fx)
            fd = int(fa1)
            fat_l.append(fd)
        fat_data = Facilities.objects.all().filter(pk__in=fat_l)
        # XXX----END-----XXXX

        #XXX---getting Activities filter data---XXX
        for ax in location_activity:
            aa1 = ast.literal_eval(ax)
            ad = int(aa1)
            act_l.append(ad)
        act_data = Activities.objects.all().filter(pk__in=act_l)
        # XXX----END-----XXXX

        #XXXXXXX-------Recommended section start--------XXXXXXXXX

        recomm_loc = Location_add.objects.all().filter(city=location_city)
        print('love : ',location_city)
        # XXXXXXXX--------END-------XXXXX

        review = Review.objects.all().filter(park_tag='local_user',park_id=id).order_by('-id')[:3]
        image = img_review()
        review_count = Review.objects.filter(park_id=id).count()

        #xxxxx------trending section------xxxxx
        trend_insert(id,'home')
        #xxxxx-----end-----xxxxx
        # XXXX----WEATHER----XXXXXX
        # wther = cweather(location_city)
        # XXXXX-----END-----XXXXXX

        # xxxx------twitter api----xxxxxxx
        twit_api = twitter(park_name,id)
        # xxxxxx-------end------xxxxxx

        # XXXXXXXX--------SEARCH DATA INSERT-------XXXXXXXXXXX
        u = request.user.is_authenticated
        if u:
            user = User.objects.get(username=request.user.username)
            Search_data(user=user,p_id=id,loc=location_city).save()
        # XXXXXXXXX---------END----------XXXXXXXXXX
        random1 = random.randint(1,5)
        safety = park_safety()
        c_safety = corona_safety(location_state)
        location_img = Img_bypublic.objects.filter(location_bypublic=id)
        logger.info(f'XXXXX----------Park detail user Method End-----XXXXXXX')
        return render(request,'park_detail_user.html',{'location_single':location_single,'cat_id':cat_data,'fat_id':fat_data,'act_id':act_data,'id':id,'review':review,'tag':'local_user','image':image,'r_cnt':review_count,'recomm_loc':recomm_loc,'random':random1,'twit_api':twit_api,'safety':safety,'c_safety':c_safety,'location_img':location_img})

# XXXXXX-----END PARK DETAILS DATA-----XXXXXXX

# XXXXXX-----Start PARK Tag DATA-----XXXXXXX
def tag_parks(request,tag):
    if tag == 'State Parks':
        near = Location_add.objects.all().filter(state='California')
    else:
        near = ''
    data = Usa_state_park_list.objects.all().filter(state='California',tag=tag)
    data113 = Sreview.objects.all().filter(state='California')
    return render(request,'state_park_list.html',{'data':data,'near':near,'state':'California','data11':data113,'tag':tag})

# XXXXXX-----END PARK Tag DATA-----XXXXXXX

# XXXXXX-----global_search Tag DATA-----XXXXXXX
def global_search(request):
    logger.info(f'Global Search Method : start')
    if request.method == 'POST':
        city = request.POST.get('serch','')
        googlenews = GoogleNews()
        googlenews = GoogleNews('en','d')
        googlenews.search(city)
        googlenews.getpage(1)
        a = googlenews.result()

        if not a:
            googlenews.search(city)
            googlenews.getpage(1)
            b = googlenews.result()
        else:
            b = a
        res_list = []
        for i in range(len(b)):
            if b[i] not in b[i + 1:]:
                res_list.append(b[i])

        hotel_data = park_city(city)
        logger.info(f'XXXXX----------Global Search Method End-----XXXXXXX')
        return render(request,'google_news.html',{'news_api':res_list,'l':a,'hotel_api':hotel_data,'msg':'Currently no news associated with this park!!!'})
    return render(request,'google_news.html',{'msg':'Get News and Updates  !!!..'})

# XXXXXX-----END PARK Tag DATA-----XXXXXXX


# XXXXXXX--------Foodie Find   -------XXXXXXXXXX
def foodie_find(request):
    logger.info(f'XXXXX----------foodie_find Method Start-----XXXXXXX')
    logger.info(f'XXXXX----------foodie_find Method End-----XXXXXXX')
    return render(request,'foodie_find.html')
# XXXXXXXX-------END Foodie Find-------XXXXXXXX


# XXXXXXX--------Foodie Find   -------XXXXXXXXXX
def food_camping(request):
    logger.info(f'XXXXX----------food_camping Method Start-----XXXXXXX')
    logger.info(f'XXXXX----------food_camping Method End-----XXXXXXX')
    return render(request,'food_camping.html')
# XXXXXXXX-------END Foodie Find-------XXXXXXXX

# XXXXXXX--------terms_conditions   -------XXXXXXXXXX
def terms_conditions(request):
    logger.info(f'XXXXX----------terms_conditions Method Start-----XXXXXXX')
    logger.info(f'XXXXX----------terms_conditions Method End-----XXXXXXX')
    return render(request,'term.html')
# XXXXXXXX-------END Foodie Find-------XXXXXXXX

# XXXXXXX--------licences   -------XXXXXXXXXX
def licences(request):
    logger.info(f'XXXXX----------licences Method Start-----XXXXXXX')
    logger.info(f'XXXXX----------licences Method End-----XXXXXXX')
    return render(request,'licence.html')
# XXXXXXXX-------END Foodie Find-------XXXXXXXX

# XXXXXXX--------privacy_policy  -------XXXXXXXXXX
def privacy_policy(request):
    logger.info(f'XXXXX----------privacy_policy Method Start-----XXXXXXX')
    logger.info(f'XXXXX----------privacy_policy Method End-----XXXXXXX')
    return render(request,'policy.html')
# XXXXXXXX-------END Foodie Find-------XXXXXXXX

# XXXXXXX--------community   -------XXXXXXXXXX
def community(request):
    logger.info(f'XXXXX----------community Method Start-----XXXXXXX')
    logger.info(f'XXXXX----------community Method End-----XXXXXXX')
    return render(request,'community.html')
# XXXXXXXX-------END Foodie Find-------XXXXXXXX

# XXXXXXXXX----------Home page data-------XXXXXXXXXX

def home_virtual_list(request):
    '''here we are fetching all data such as virtual, activiy, facility and tags'''
    logger.info(' Home Method : Retreving Virtual Location')
    virtual = Virtual.objects.all()
    # todo next line is to be commented
    logger.info(' Home Method : Retreving Guideline_detail ')
    guideline_detail = Guideline_detail.objects.all().filter(typ='Virtually')
    return render(request,'virtual_list.html',{'virtual':virtual,'guideline_detail':guideline_detail})

def home_activity_list(request):
    logger.info(' Home Method : Retreving Activities ')
    activity = Activities.objects.all().order_by('-count').filter(~Q(count=0))
    logger.info(' Home Method : Retreving Guideline_detail ')
    guideline_detail = Guideline_detail.objects.all().filter(typ='Activities')
    return render(request,'activity.html',{'activity':activity,'guideline_detail':guideline_detail})

def home_facility_list(request):
    logger.info(' Home Method : Retreving Facilities ')
    facility = Facilities.objects.all().order_by('-count').filter(~Q(count=0))
    logger.info(' Home Method : Retreving Guideline_detail ')
    guideline_detail = Guideline_detail.objects.all().filter(typ='Facility')
    return render(request,'facility.html',{'facility':facility,'guideline_detail':guideline_detail})

def home_tag_list(request):
    logger.info(' Home Method : Retreving Park tag ')
    tag = Park_tag.objects.all()
    logger.info(' Home Method : Retreving Guideline_detail ')
    guideline_detail = Guideline_detail.objects.all().filter(typ='tags')
    return render(request,'tags.html',{'tag':tag,'guideline_detail':guideline_detail})

def slider_l(request):
    return render(request,'slider_l.html')

def slider_m(request):
    return render(request,'slider_m.html')


# XXXXXXXX---------END HOME PAGE DATA------XXXXXXX
