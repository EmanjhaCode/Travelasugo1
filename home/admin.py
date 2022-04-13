from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from emanjha_admin.models import Park_tag

# Register your models here.
@admin.register(Usa_state_park_list)
class Usa_state_park_listAdmin(ImportExportModelAdmin):
    list_display = ['id','name','link','tag','state','imagelinks']

@admin.register(Park_activity)
class Park_activityAdmin(ImportExportModelAdmin):
    list_display = ['id','park_id','activity','name']

@admin.register(Img_activity)
class Img_activityAdmin(ImportExportModelAdmin):
    list_display = ['id','activity','img']

@admin.register(Sreview)
class SreviewAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Location_bypublic)
class Location_bypublicAdmin(ImportExportModelAdmin):
    list_display = ['id','park_name']

@admin.register(Img_bypublic)
class Img_bypublicAdmin(ImportExportModelAdmin):
    list_display = ['id','location_bypublic','img']

@admin.register(Alabama)
class AlabamaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Alaska)
class AlaskaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Samoa)
class SamoaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Arizona)
class ArizonaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Arkansas)
class ArkansasAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']


@admin.register(Colorado)
class ColoradoAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Connecticut)
class ConnecticutAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Delaware)
class DelawareAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Dcolumbia)
class DcolumbiaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Florida)
class FloridaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Georgia)
class GeorgiaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Guam)
class GuamAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Hawaii)
class HawaiiAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Idaho)
class IdahoAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Illinois)
class IllinoisAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Indiana)
class IndianaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Iowa)
class IowaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Kansas)
class KansasAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Kentucky)
class KentuckyAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Louisiana)
class LouisianaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Maine)
class MaineAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Maryland)
class MarylandAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Massachusetts)
class MassachusettsAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Michigan)
class MichiganAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Minnesota)
class MinnesotaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Mississippi)
class MississippiAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Missouri)
class MissouriAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Montana)
class MontanaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Nebraska)
class NebraskaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Nevada)
class NevadaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Hampshire)
class HampshireAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Jersey)
class JerseyAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Mexico)
class MexicoAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(NewYork)
class NewYorkAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(NorthCarolina)
class NorthCarolinaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(NorthDakota)
class NorthDakotaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Mariana)
class MarianaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Ohio)
class OhioAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Oklahoma)
class OklahomaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Oregon)
class OregonAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Pennsylvania)
class PennsylvaniaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Puerto)
class PuertoAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Rhode)
class RhodeAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(SouthCarolina)
class SouthCarolinaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(SouthDakota)
class South_DakotaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Tennessee)
class TennesseeAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Texas)
class TexasAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Utah)
class UtahAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Vermont)
class VermontAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Virgin)
class VirginAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Virginia)
class VirginiaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Washington)
class WashingtonAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(WestVirginia)
class WestVirginiaAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Wisconsin)
class WisconsinAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Wyoming)
class WyomingAdmin(ImportExportModelAdmin):
    list_display = ['id','pid','tag','state','overall','service','behaviour','comment', 'user_nm','img','p_date']

@admin.register(Park_tag)
class Park_tagAdmin(ImportExportModelAdmin):
    list_display = ['nm','img']
