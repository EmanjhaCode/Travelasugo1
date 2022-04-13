from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from home.models import California
from .models import *


# Register your models here.
@admin.register(California)
class CaliforniaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Guideline)
class GuidelineAdmin(ImportExportModelAdmin):
    list_display = ['id','nm','guide','img','img_status']

@admin.register(Guideline_detail)
class Guideline_detailAdmin(ImportExportModelAdmin):
    list_display = ['id','guideline','typ','guide_detail1','img1','guide_detail2','img2','guide_detail3','img3']

@admin.register(park_list_backup)
class park_list_backupAdmin(ImportExportModelAdmin):
    list_display = ['id','name','link','tag','state','imagelinks']
