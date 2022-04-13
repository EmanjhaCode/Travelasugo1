from django.db import models

# Create your models here.
class Facilities(models.Model):
    name=models.CharField(max_length=200)
    count=models.IntegerField(default=0)
    history=models.CharField(max_length=2000, default="empty")
    image=models.FileField(upload_to='facilities',default="")

class Activities(models.Model):
    name=models.CharField(max_length=200)
    count=models.IntegerField(default=0)
    history=models.CharField(max_length=2000, default="empty")
    image=models.FileField(upload_to='activities',default="")


class Categories(models.Model):
    name=models.CharField(max_length=500)
    history=models.CharField(max_length=2000, default="empty")
    image=models.FileField(upload_to='categories',default="")

class Api_document(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    api_url = models.CharField(max_length=200)

class Location_add(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=400)
    logitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    overview = models.CharField(max_length=1000)
    category = models.CharField(max_length=2000)
    facility = models.CharField(max_length=2000)
    activity = models.CharField(max_length=2000)
    thumbnail1=models.FileField(upload_to='thumbnail1',default="")
    thumbnail2=models.FileField(upload_to='thumbnail2',default="")
    thumbnail3=models.FileField(upload_to='thumbnail3',default="")
    other1=models.FileField(upload_to='other1',default="")
    other2=models.FileField(upload_to='other2',default="")
    other3=models.FileField(upload_to='other3',default="")

class Usa_state(models.Model):
    name = models.CharField(max_length=120)
    api_url = models.CharField(max_length=300)
    img=models.FileField(upload_to='state_img',default="none")
    desc = models.CharField(max_length=280,default="none")
    park_qnt = models.CharField(max_length=200,default="none")

class Virtual(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=2000, default="empty")
    image=models.FileField(upload_to='virtual',default="")
    url=models.CharField(max_length=200)

class Covid_state_link(models.Model):
    usa_state = models.CharField(max_length=200)
    link = models.CharField(max_length=500)

class Park_tag(models.Model):
    nm = models.CharField(max_length=100)
    img = models.CharField(max_length=500)

TITLE_CHOICES = [
    ('Active Image', 'active'),
    ('Block Image','block'),

]


class Guideline(models.Model):
    nm = models.CharField(max_length=20)
    guide = models.CharField(max_length=150)
    img=models.FileField(upload_to='Guideline_img',default="")
    img_status = models.CharField(max_length=20,choices=TITLE_CHOICES, default='block')
    def __str__(self):
        return self.guide,self.nm
class Guideline_detail(models.Model):
    guideline = models.CharField(max_length=350)
    typ = models.CharField(max_length=350,default="")
    guide_detail1 = models.CharField(max_length=650)
    img1=models.FileField(upload_to='guideline_detail1',default="")
    guide_detail2 = models.CharField(max_length=650)
    img2=models.FileField(upload_to='guideline_detail2',default="")
    guide_detail3 = models.CharField(max_length=650)
    img3=models.FileField(upload_to='guideline_detail3',default="")

class park_list_backup(models.Model):
    name = models.CharField(max_length=800, default='none',db_index=True)
    link = models.CharField(max_length=800, default='none')
    tag = models.CharField(max_length=200, default='none')
    state = models.CharField(max_length=100, default='none')
    imagelinks = models.CharField(max_length=1000, default='none')
