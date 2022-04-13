from django.db import models

# Create your models here.

class SignUp(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    activity = models.CharField(max_length=800)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    otp = models.CharField(max_length=10)

class Review(models.Model):
    user_id = models.CharField(max_length=150)
    park_id = models.CharField(max_length=30)
    park_tag = models.CharField(max_length=20)
    overall = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    behaviour = models.CharField(max_length=20)
    comment = models.CharField(max_length=500)
    user_nm = models.CharField(max_length=50,default='none')
    p_date = models.CharField(max_length=20)

class Imd_Review(models.Model):
    rid = models.CharField(max_length=150)
    img = models.ImageField(upload_to='review',
                              verbose_name='Image')

class Feedback(models.Model):
    nm = models.CharField(max_length=100)
    em = models.CharField(max_length=100)
    feed = models.CharField(max_length=2000)
    p_date = models.CharField(max_length=20)

class Wishlist(models.Model):
    p_id = models.IntegerField()
    tag = models.CharField(max_length=10)
    u_id = models.CharField(max_length=100)

class Trending(models.Model):
    p_id = models.CharField(max_length=100)
    tag = models.CharField(max_length=10)
    dt = models.CharField(max_length=100)
    qnt = models.IntegerField()

class Twitter(models.Model):
    p_id = models.IntegerField()
    twit_text = models.CharField(max_length=2500,default='none')
    dt = models.CharField(max_length=50,default='none')
    twit_count = models.CharField(max_length=20,default='none')
    twit_id = models.CharField(max_length=100,default='none')
    twit_img = models.CharField(max_length=200,default='none')
    twit_user1 = models.CharField(max_length=100,default='none')
    twit_user2 = models.CharField(max_length=100,default='none')
    twit_like = models.CharField(max_length=20,default='none')
    twit_date = models.CharField(max_length=100,default='02-09-2020')

class Park_hotel(models.Model):
    p_id = models.IntegerField()
    h_name = models.CharField(max_length=1000, default='none')
    h_img = models.CharField(max_length=500, default='none')
    km = models.FloatField()
    cat = models.CharField(max_length=200, default='none')

class Park_hotel_city(models.Model):
    h_name = models.CharField(max_length=1000, default='none')
    h_img = models.CharField(max_length=500, default='none')
    cat = models.CharField(max_length=200, default='none')
    city = models.CharField(max_length=200, default='none')

class Search_data(models.Model):
    p_id=models.IntegerField()
    loc = models.CharField(max_length=200, default='none')
    user = models.CharField(max_length=200, default='none')


class Safety_data(models.Model):
    title = models.CharField(max_length=200, default='none')
    des = models.CharField(max_length=2000, default='none')
    tag = models.CharField(max_length=200, default='none')

class Usa_state_park_list(models.Model):
    name = models.CharField(max_length=800, default='none',db_index=True)
    link = models.CharField(max_length=800, default='none')
    tag = models.CharField(max_length=200, default='none')
    state = models.CharField(max_length=100, default='none')
    imagelinks = models.CharField(max_length=1000, default='none')
    

class Usa_park_list_ded(models.Model):
    list_id = models.IntegerField()
    city = models.CharField(max_length=100, default='none')
    country = models.CharField(max_length=100, default='none')
    zip = models.CharField(max_length=50, default='none')
    address = models.CharField(max_length=800, default='none')
    lat = models.CharField(max_length=100, default='none')
    lon = models.CharField(max_length=100, default='none')
    overview = models.CharField(max_length=2000, default='none')
    neartown = models.CharField(max_length=2000, default='none')
    facility = models.CharField(max_length=2000, default='none')
    activity = models.CharField(max_length=2000, default='none')
    direction = models.CharField(max_length=2000, default='none')
    nearby = models.CharField(max_length=2000, default='none')

class Sreview(models.Model):
    pid = models.IntegerField()
    tag = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    overall = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    behaviour = models.CharField(max_length=20)
    comment = models.CharField(max_length=1200)
    user_nm = models.CharField(max_length=50,default='none')
    img = models.CharField(max_length=1200)
    p_date = models.CharField(max_length=20)

class Park_activity(models.Model):
    park_id = models.IntegerField(db_index=True)
    activity = models.CharField(max_length=20)
    name = models.CharField(max_length=30)


class Img_activity(models.Model):
    activity = models.CharField(db_index=True,max_length=50)
    img = models.CharField(max_length=500)

class Location_bypublic(models.Model):
    park_name = models.CharField(max_length=300)
    user_name = models.CharField(max_length=50)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=400)
    logitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    overview = models.CharField(max_length=1500)
    category = models.CharField(max_length=2000)
    facility = models.CharField(max_length=2000)
    activity = models.CharField(max_length=2000)
    status = models.CharField(max_length=20,default='block')
    img = models.ImageField(upload_to='bypublic1',
                              verbose_name='Image')


class Img_bypublic(models.Model):
    location_bypublic = models.ForeignKey('Location_bypublic',on_delete=models.CASCADE)
    img = models.ImageField(upload_to='bypublic',
                              verbose_name='Image')


class Commonfield(models.Model):
    pid = models.IntegerField(db_index=True)
    tag = models.CharField(max_length=20,default='none',null= True)
    state = models.CharField(max_length=30,default='none',null= True)
    overall = models.CharField(max_length=20,default='none',null= True)
    service = models.CharField(max_length=20,default='none',null= True)
    behaviour = models.CharField(max_length=20,default='none',null= True)
    comment = models.CharField(max_length=1200,default='none',null= True)
    user_nm = models.CharField(max_length=50,default='none',null= True)
    img = models.CharField(max_length=1200,default='none',null= True)
    p_date = models.CharField(max_length=20,default='none',null= True)
    class Meta:
        abstract = True

class Alabama(Commonfield):
    pass

class Alaska(Commonfield):
    pass

class Samoa(Commonfield):
    pass

class Arizona(Commonfield):
    pass

class Arkansas(Commonfield):
    pass

class California(Commonfield):
    pass

class Colorado(Commonfield):
    pass

class Connecticut(Commonfield):
    pass

class Delaware(Commonfield):
    pass

class Dcolumbia(Commonfield):
    pass

class Florida(Commonfield):
    pass

class Georgia(Commonfield):
    pass

class Guam(Commonfield):
    pass

class Hawaii(Commonfield):
    pass

class Idaho(Commonfield):
    pass

class Illinois(Commonfield):
    pass

class Indiana(Commonfield):
    pass

class Iowa(Commonfield):
    pass

class Kansas(Commonfield):
    pass

class Kentucky(Commonfield):
    pass

class Louisiana(Commonfield):
    pass

class Maine(Commonfield):
    pass

class Maryland(Commonfield):
    pass

class Massachusetts(Commonfield):
    pass

class Michigan(Commonfield):
    pass

class Minnesota(Commonfield):
    pass

class Mississippi(Commonfield):
    pass

class Missouri(Commonfield):
    pass

class Montana(Commonfield):
    pass

class Nebraska(Commonfield):
    pass

class Nevada(Commonfield):
    pass

class Hampshire(Commonfield):
    pass

class Jersey(Commonfield):
    pass

class Mexico(Commonfield):
    pass

class NewYork(Commonfield):
    pass

class NorthCarolina(Commonfield):
    pass

class NorthDakota(Commonfield):
    pass

class Mariana(Commonfield):
    pass

class Ohio(Commonfield):
    pass

class Oklahoma(Commonfield):
    pass

class Oregon(Commonfield):
    pass

class Pennsylvania(Commonfield):
    pass

class Puerto(Commonfield):
    pass

class Rhode(Commonfield):
    pass

class SouthCarolina(Commonfield):
    pass

class SouthDakota(Commonfield):
    pass

class Tennessee(Commonfield):
    pass

class Texas(Commonfield):
    pass

class Utah(Commonfield):
    pass

class Vermont(Commonfield):
    pass

class Virgin(Commonfield):
    pass

class Virginia(Commonfield):
    pass

class Washington(Commonfield):
    pass

class WestVirginia(Commonfield):
    pass

class Wisconsin(Commonfield):
    pass

class Wyoming(Commonfield):
    pass
