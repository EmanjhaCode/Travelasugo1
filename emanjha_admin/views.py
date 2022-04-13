from django.shortcuts import render, redirect
from .models import *
from home.models import Feedback, Safety_data,Location_bypublic,Img_bypublic,Park_activity,Usa_state_park_list
from .serializers import FacilitiesSerializer, ActivitiesSerializer, CategoriesSerializer,LocationSerializer, StateSerializer
from django.http import HttpResponse
from rest_framework import viewsets
from array import *
import json, requests
import ast
from django.contrib.auth.models import User, auth
import urllib.request
from django.http import JsonResponse
import os
from .alphabet import *
from django.conf import settings
import pickle
from django import template
register = template.Library()


# https://api.flightapi.io/dashboard/5f293c94db9e9a675a0ed374 flight api
# XXXXXX-----Admin Login Section-----XXXXXXXX
def login(request):
    if request.method=='POST':
        unm=request.POST['unm']
        ps=request.POST['ps']
        user = auth.authenticate(username=unm,password=ps)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request,'login.html',{'msg':'User Name Not Exits..!'})

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/login')
# XXXX----END LOGIN SECTION---XXXX

# Admin Panel Dashboad section start here
def dashboard(request):
    return render(request,'dashboard.html')

# Admin Panel Dashboard end here


# XXXXXXXX---------  Start Facilities Section --------XXXXXXXXX

 # Facilities API start here
class FacilitiesView(viewsets.ModelViewSet):
    """API URLS FOR VIEW Facilities API : http://127.0.0.1:8000/facilities_api"""
    queryset = Facilities.objects.all()
    serializer_class = FacilitiesSerializer
 # Facilities API END

def facilities(request):
    # Here we do Facilities add to db section
    if request.method =='POST':
        name = request.POST.get('name','empty')
        history = request.POST.get('history','empty')
        image = request.FILES.get('image','image_empty')
        insert = Facilities(name=name,image=image,history=history)
        insert.save()
        return render(request,'facilities.html',{'msg':'Facilities Added Successfully..'})
        # end Facilities add to db section
    else:
        data = Facilities.objects.all().order_by('-id')
        return render(request,'facilities.html',{'data':data})

    # facilities_delete section start
def facilities_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Facilities.objects.filter(id=id).delete()
        return render(request,'facilities.html',{'msg':'Facilities Deleted Successfully..'})
    # end facilities_delete section

# facility update section start
def facilities_update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nm = request.POST.get('nm')
        history = request.POST.get('history')
        img1 = request.POST.get('img1')
        img = request.FILES.get('img',img1)
        Facilities(name=nm,image=img,history=history,id=id).save()
        return render(request,'facilities.html',{'msg':'Facilities Updated Successfully..'})

# facility update section end

# XXXXXXXX------- End Facilities -------XXXXXXXXX

# XXXXXXXXXX------- Start Activities Section -------XXXXXXXXXX

# Activities API start here
class ActivitiesView(viewsets.ModelViewSet):
   """API URLS FOR VIEW Activities API : http://127.0.0.1:8000/activities_api"""
   queryset = Activities.objects.all()
   serializer_class = ActivitiesSerializer


 # Activities API END
def activities(request):
    # Here we do Activities add to db section
    if request.method =='POST':
        name = request.POST.get('name','empty')
        history = request.POST.get('history','empty')
        image = request.FILES.get('image','image_empty')
        insert = Activities(name=name,image=image,history=history)
        insert.save()
        return render(request,'activities.html',{'msg':'Activities Added Successfully..'})
        # end Activities add to db section
    else:
        data = Activities.objects.all().order_by('-id')
        return render(request,'activities.html',{'data':data})

    # Activities delete section start
def activities_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Activities.objects.filter(id=id).delete()
        return render(request,'activities.html',{'msg':'Activities Deleted Successfully..'})
    # end Activities delete section

# Activities update section start
def activities_update(request):
  if request.method == 'POST':
      id = request.POST.get('id')
      nm = request.POST.get('nm')
      history = request.POST.get('history')
      img1 = request.POST.get('img1')
      img = request.FILES.get('img',img1)
      Activities(name=nm,image=img,history=history,id=id).save()
      return render(request,'activities.html',{'msg':'Activities Updated Successfully..'})

# Activities update section end

#  XXXXXXX-------- End Activities -------XXXXXXX


# XXXXXXXX---------  Start Categories Section --------XXXXXXXXX

 # Categories API start here
class CategoriesView(viewsets.ModelViewSet):
    """API URLS FOR VIEW Categories API : http://127.0.0.1:8000/categories_api"""
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
 # Categories API END

def categories(request):
    # Here we do Categories add to db section
    if request.method =='POST':
        name = request.POST.get('name','empty')
        history = request.POST.get('history','empty')
        image = request.FILES.get('image','image_empty')
        insert = Categories(name=name,image=image,history=history)
        insert.save()
        return render(request,'categories.html',{'msg':'Categories Added Successfully..'})
        # end Categories add to db section
    else:
        data = Categories.objects.all().order_by('-id')
        return render(request,'categories.html',{'data':data})

    # Categories_delete section start
def categories_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Categories.objects.filter(id=id).delete()
        return render(request,'categories.html',{'msg':'Categories Deleted Successfully..'})
    # end Categories_delete section

# Categories update section start
def categories_update(request):
  if request.method == 'POST':
      id = request.POST.get('id')
      nm = request.POST.get('nm')
      history = request.POST.get('history')
      img1 = request.POST.get('img1')
      img = request.FILES.get('img',img1)
      Categories(name=nm,image=img,history=history,id=id).save()
      return render(request,'categories.html',{'msg':'Categories Updated Successfully..'})

# Categories update section end

# XXXXXXXX------- End Categories -------XXXXXXXXX

# XXXXXXXXXX-------API DOCUMENTS SECTION START-------XXXXXXXXXXXX

def api_document(request):
    if request.method =='POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        api_url = request.POST.get('api_url')
        insert = Api_document(name=name,desc=desc,api_url=api_url).save()
        return render(request,'document.html',{'msg':'Documents Added Successfully....!'})
    else:
        data = Api_document.objects.all()
        return render(request,'document.html',{'data':data})

# XX---END DOCUMENY---XX

# XXXXXX---------START LOCATION Section------------XXXXXXXXXXXXXX

# Categories API start here
class LocationView(viewsets.ModelViewSet):
   """API URLS FOR VIEW LocationSerializer API : http://127.0.0.1:8000/location_api"""
   queryset = Location_add.objects.all()
   serializer_class = LocationSerializer
# Categories API END

#XXXXXX-------Start all Location Section----XXXXX
def location(request):
    location_data = Location_add.objects.all().order_by('-id')
    return render(request,'location.html',{'data':location_data})

#XXX----End all Location---XXX

#XXX---Start single-location Section---XXX
def single_location(request, id):
    location_single = Location_add.objects.all().filter(id=id)


    for cat_id in location_single:
        location_cat = cat_id.category
        location_category = location_cat.strip('][').split(', ')

        location_fat = cat_id.facility
        location_facility = location_fat.strip('][').split(', ')

        location_act = cat_id.activity
        location_activity = location_act.strip('][').split(', ')


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

    return render(request,'single-location.html',{'location_single':location_single,'cat_id':cat_data,'fat_id':fat_data,'act_id':act_data})

#XXX---End single-location---XXX

#XXXX-----START ADD LOCATION SECTION----XXXXX
def add_location(request):
    if request.method == 'POST':
        name = request.POST.get('name','name_empty')
        city = request.POST.get('city','city_empty')
        state = request.POST.get('state','state_empty')
        country = request.POST.get('country','country_empty')
        zipcode = request.POST.get('zipcode','zipcode_empty')
        address = request.POST.get('address','address_empty')
        logitude = request.POST.get('logitude','logitude_empty')
        latitude = request.POST.get('latitude','latitude_empty')
        overview = request.POST.get('overview','name_empty')
        categories = request.POST.getlist('category','category_empty')
        facilities = request.POST.getlist('facility','facility_empty')
        activities = request.POST.getlist('activity','activity_empty')
        thumbnail1 = request.FILES.get('thumbnail1','thumbnail1_empty')
        thumbnail2 = request.FILES.get('thumbnail2','thumbnail2_empty')
        thumbnail3 = request.FILES.get('thumbnail3','thumbnail3_empty')
        other1 = request.FILES.get('other1','other1_empty')
        other2 = request.FILES.get('other2','other2_empty')
        other3 = request.FILES.get('other3','other3_empty')
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

        Location_add(name=name,city=city,state=state,country=country,zipcode=zipcode,address=address,logitude=logitude,
        latitude=latitude,overview=overview,category=c1,facility=f1,activity=a1,
        thumbnail1=thumbnail1,thumbnail2=thumbnail2,thumbnail3=thumbnail3,other1=other1,
        other2=other2,other3=other3).save()
        return render(request,'add_location.html',{'msg':'Location Added Successfully..!'})

    else:
        facility = Facilities.objects.all().order_by('-id')
        activity = Activities.objects.all().order_by('-id')
        category = Categories.objects.all()
        return render(request,'add_location.html',{'facility_data':facility,'activity_data':activity,'category_data':category})

#XXX---END ADD LOCATION SECTION---XXX

# location_delete section start
def location_delete(request,id):
    delete = Location_add.objects.filter(id=id).delete()
    return render(request,'location.html',{'msg':'Deleted Successfully..'})
# end location_delete section
# XXXXXXXXXX--------END LOCATION Section---------XXXXXXXXXXX

# XXXXXXXXXX---------LOCATION UPDATE START-------XXXXXXXXXXXX
def location_update(request):
    id = request.POST.get('id')
    name = request.POST.get('name','name_empty')
    city = request.POST.get('city','city_empty')
    state = request.POST.get('state','state_empty')
    country = request.POST.get('country','country_empty')
    zipcode = request.POST.get('zipcode','zipcode_empty')
    address = request.POST.get('address','address_empty')
    logitude = request.POST.get('logitude','logitude_empty')
    latitude = request.POST.get('latitude','latitude_empty')
    overview = request.POST.get('overview','name_empty')
    Location_add.objects.filter(id=id).update(name=name,city=city,state=state,country=country,zipcode=zipcode,address=address,logitude=logitude,
    latitude=latitude,overview=overview)
    return render(request,'location.html',{'msg':'Update Successfully..'})
# XXXXXXXXX----------END----------XXXXXXXXXX

# XXXXXXXXX------US STATE UPS API------XXXXXXXXXXXXX

# STATE API start here
class UstateView(viewsets.ModelViewSet):
   """API URLS FOR VIEW State API : http://127.0.0.1:8000/usa_state_api"""
   queryset = Usa_state.objects.all()
   serializer_class = StateSerializer
# STATE API END

# XXX---ADD US STATE---XXXX
def add_us_state(request):
    if request.method == 'POST':
        name = request.POST.get('name','state name not found')
        url = request.POST.get('url','url not found')
        Usa_state(name=name,api_url=url).save()
        return render(request,'add_state.html',{'msg':'Added Successfully..'})
    else:
        data = Usa_state.objects.all()
        return render(request,'add_state.html',{'data':data})

# XXX---END ADD STATE--XX

#  STATE update section start
def state_update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name','state name not found')
        url = request.POST.get('api_url','url not found')
        img1 = request.POST.get('img1')
        img = request.FILES.get('img',img1)
        desc = request.POST.get('desc')
        park_qnt = request.POST.get('park_qnt')
        Usa_state(name=name,api_url=url,img=img,desc=desc,park_qnt=park_qnt,id=id).save()
        return render(request,'add_state.html',{'msg':f'Updated Successfully'})

# end  update delete section

#  STATE delete section start
def state_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Usa_state.objects.filter(id=id).delete()
        return render(request,'add_state.html',{'msg':'Deleted Successfully..'})
# end  STATE delete section

def us_state_api(request,name):
    url = f"https://developer.nps.gov/api/v1/parks?stateCode={name}&api_key=raLnxkuep5zAv2tSiySQgxCqXU1NSzZ24Cl1YmY5"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return JsonResponse(data)


# XXX---Single api us state---XXXX
def us_state_single_api(request,name):
    url = f"https://developer.nps.gov/api/v1/parks?parkCode={name}&api_key=raLnxkuep5zAv2tSiySQgxCqXU1NSzZ24Cl1YmY5"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return JsonResponse(data)
# end

# XXX---Alphabet api us state---XXXX
def us_state_alphabet_api(request,name):
    name = name.lower()
    d = alphabet(name)
    url = f"https://developer.nps.gov/api/v1/parks?parkCode={d}&api_key=raLnxkuep5zAv2tSiySQgxCqXU1NSzZ24Cl1YmY5"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return JsonResponse(data)
# end

# XXXX---END US STATE UPS API---XXX


# XXXXXXX-------- start Virtual -------XXXXXXX
def virtual_add(request):
    # Here we do Virtual add to db section
    if request.method =='POST':
        name = request.POST.get('name','empty')
        history = request.POST.get('history','empty')
        url = request.POST.get('url','empty')
        image = request.FILES.get('image','image_empty')
        insert = Virtual(name=name,image=image,description=history,url=url)
        insert.save()
        return render(request,'virtual.html',{'msg':'Virtual Added Successfully..'})
        # end Virtual add to db section
    else:
        data = Virtual.objects.all().order_by('-id')
        return render(request,'virtual.html',{'data':data})

    # Virtual delete section start
def virtual_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Virtual.objects.filter(id=id).delete()
        return render(request,'virtual.html',{'msg':'Virtual Deleted Successfully..'})
    # end Virtual delete section

# Virtual update section start
def virtual_update(request):
  if request.method == 'POST':
      id = request.POST.get('id')
      nm = request.POST.get('nm')
      url = request.POST.get('url','empty')
      history = request.POST.get('history')
      Virtual.objects.filter(id=id).update(name=nm,description=history,url=url)
      return render(request,'virtual.html',{'msg':'Virtual Updated Successfully..'})

# Virtual update section end


#  XXXXXXX-------- End Virtual -------XXXXXXX

# XXXXX-------FEEDBACK-------XXXXXXXXXX
def admin_feedback(request):
    data = Feedback.objects.all()
    return render(request,'admin_feedback.html',{'data':data})

# admin_feedback delete section start
def feedback_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Feedback.objects.filter(id=id).delete()
        return render(request,'admin_feedback.html',{'msg':'Feedback Deleted Successfully..'})

# XXXX----END-------XXXXX

# XXXXXXXX-----------START SAFETY SECTION--------XXXXXXXXXXX

def safety(request):
    # Here we do SAFETY add to db section
    if request.method =='POST':
        name = request.POST.get('name','empty')
        des = request.POST.get('des','empty')
        tag = request.POST.get('tag','empty')
        insert = Safety_data(title=name,des=des,tag=tag)
        insert.save()
        return render(request,'safety.html',{'msg':'Safety Added Successfully..'})
        # end SAFETY add to db section
    else:
        data = Safety_data.objects.all().order_by('-id')
        return render(request,'safety.html',{'data':data})

    # SAFETY_delete section start
def safety_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Safety_data.objects.filter(id=id).delete()
        return render(request,'safety.html',{'msg':'Safety Deleted Successfully..'})
    # end SAFETY_delete section

# SAFETY update section start
def safety_update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nm = request.POST.get('nm')
        des = request.POST.get('des')
        tag = request.POST.get('tag')
        Safety_data.objects.filter(id=id).update(title=nm,des=des,tag=tag)
        return render(request,'safety.html',{'msg':'Safety Updated Successfully..'})

# SAFETY update section end

# XXXXXXXX------- End SAFETY -------XXXXXXXXX

# XXXXXXXX--------- START COVID LINK SECTION---------XXXXXXXXXXXX
def covid_state_link(request):
    state = Usa_state.objects.all()
    if request.method =='POST':
        link = request.POST.get('link','empty')
        usa_state = request.POST.get('usa_state','empty')
        insert = Covid_state_link(link=link,usa_state=usa_state)
        insert.save()
        return render(request,'covid_link.html',{'msg':'COVID state link Added Successfully..'})
        # end SAFETY add to db section
    else:
        data = Covid_state_link.objects.all().order_by('-id')
        return render(request,'covid_link.html',{'data':data,'state':state})


# XXXXXXXXXXXX-----------END---------------

# covid_link delete section start
def covid_state_link_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Covid_state_link.objects.filter(id=id).delete()
        return render(request,'covid_link.html',{'msg':'COVID state link Deleted Successfully..'})
# end SAFETY_delete section

# covid_link update section start
def covid_state_link_update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        link = request.POST.get('link')
        usa_state = request.POST.get('usa_state')
        Covid_state_link.objects.filter(id=id).update(link=link,usa_state=usa_state)
        return render(request,'covid_link.html',{'msg':'COVID state link Updated Successfully..'})

# covid_link update section end

# XXXXXXXXX-----------COVID LINK END--------XXXXXXXXXX


#   XXXXXXXXX-------------USER LOCATION------XXXXXXXXXXX

#XXXXXX-------Start all Location by user Section----XXXXX
def user_location(request):
    location_data = Location_bypublic.objects.all().order_by('-id')
    return render(request,'user_location.html',{'data':location_data})

#XXX----End all Location by user ---XXX

#XXX---Start single-location by user Section---XXX
def user_single_location(request, id):
    location_single = Location_bypublic.objects.all().filter(id=id)
    image = Img_bypublic.objects.all().filter(location_bypublic=id)


    for cat_id in location_single:
        location_cat = cat_id.category
        location_category = location_cat.strip('][').split(', ')

        location_fat = cat_id.facility
        location_facility = location_fat.strip('][').split(', ')

        location_act = cat_id.activity
        location_activity = location_act.strip('][').split(', ')


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

    return render(request,'user_single_location.html',{'location_single':location_single,'cat_id':cat_data,'fat_id':fat_data,'act_id':act_data,'image':image})

#XXX---End user-location---XXX

# XXXXXXXXXX---------Block user UPDATE status-------XXXXXXXXXXXX
def location_block(request):
    id = request.POST.get('id')
    status = request.POST.get('status','name_empty')
    if status == 'block':
        Location_bypublic.objects.filter(id=id).update(status='unblock')
    else:
        Location_bypublic.objects.filter(id=id).update(status='block')


    return render(request,'user_location.html',{'msg':'Update Successfully..'})
# XXXXXXXXX----------END----------XXXXXXXXXX

# user location_delete section start
def user_location_delete(request,id):
    delete = Location_bypublic.objects.filter(id=id).delete()
    return render(request,'user_location.html',{'msg':'Deleted Successfully..'})
# end user location_delete section

# Activity_all Section START


def all_activity(request):
    location = Usa_state_park_list.objects.values_list().filter(state='California')
    location_id = []
    for i in location:
        location_id.append(i[0])
    d1 = []
    data = Park_activity.objects.all().filter(park_id__in=location_id)
    for d in data:
        d1.append(d.activity)
    print(d1)    
    return render(request,'all_activity.html',{'data':data})

    # activity_all delete section start
def all_activity_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Park_activity.objects.filter(activity=id).delete()
        return render(request,'all_activity.html',{'msg':'Activity Deleted Successfully..'})
    # end Categories_delete section

# activity_all update section start
def all_activity_update(request):
  if request.method == 'POST':
      id = request.POST.get('id')
      activity_scrp = request.POST.get('activity')
      nm = request.POST.get('nm')
      Park_activity.objects.filter(id=id).update(activity=activity_scrp,name=nm)
      return render(request,'all_activity.html',{'msg':'Activity Updated Successfully..'})

# activity_all update section end
