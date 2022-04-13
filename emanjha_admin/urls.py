from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('facilities_api',views.FacilitiesView)
router.register('activities_api',views.ActivitiesView)
router.register('categories_api',views.CategoriesView)
router.register('location_api',views.LocationView)
router.register('usa_state_api',views.UstateView)





urlpatterns = [
# path('testing', views.testing, name='testing'),

path('login', views.login, name='login'),
path('logout', views.logout, name='logout'),
path('', views.dashboard, name='dashboard'),
path('api_document', views.api_document, name='api_document'),
path('', include(router.urls)),

# XXXXX-----FACILITIES SECTION FOR URL-----XXXXXX
path('facilities', views.facilities, name='facilities'),
path('facilities_delete', views.facilities_delete, name='facilities_delete'),
path('facilities_update', views.facilities_update, name='facilities_update'),

# XXX--END FACILITIES Section--XXX

# XXXXX-----Activities SECTION FOR URL-----XXXXXX
path('activities', views.activities, name='activities'),
path('activities_delete', views.activities_delete, name='activities_delete'),
path('activities_update', views.activities_update, name='activities_update'),
# XXX--END Activities Section--XXX

# XXXXX-----Categories SECTION FOR URL-----XXXXXX
path('categories', views.categories, name='categories'),
path('categories_delete', views.categories_delete, name='acategories_delete'),
path('categories_update', views.categories_update, name='categories_update'),
# XXX--END Categories Section--XXX

# XXXXX-----all_activity SECTION FOR URL-----XXXXXX
path('all_activity', views.all_activity, name='all_activity'),
path('all_activity_delete', views.all_activity_delete, name='all_activity_delete'),
path('all_activity_update', views.all_activity_update, name='all_activity_update'),
# XXX--END all_activity Section--XXX

# XXXXXX-------LOCATION SECTION START-------XXXXXXXX
path('location', views.location, name='location'),
path('add_location',views.add_location, name='add location'),
path('single-location/<int:id>', views.single_location, name='single_location'),
path('location_delete/<int:id>', views.location_delete, name='location_delete'),
path('location_update', views.location_update, name='location_update'),
path('user_location', views.user_location, name='user_location'),
path('user-single-location/<int:id>', views.user_single_location, name='user_single_location'),
path('location_block', views.location_block, name='location_block'),
path('user_location_delete/<int:id>', views.user_location_delete, name='user_location_delete'),

# XXX----END LOCATION Section---XXXX

# XXXXXXXXX---START UPS API SECTION---XXXXXXXXXX
path('us-state-api/<str:name>',views.us_state_api, name='us_state_api'),
path('add_us_state', views.add_us_state, name='add_us_state'),
path('state_delete', views.state_delete, name='state_delete'),
path('us-state-single-api/<str:name>',views.us_state_single_api, name='us_state_single_api'),
path('us-state-alphabet-api/<str:name>',views.us_state_alphabet_api, name='us_state_alphabet_api'),
path('state_update', views.state_update, name='state_update'),


# XXXX---END UPS API---XXXX

# XXXXX-----Virtual SECTION FOR URL-----XXXXXX
path('virtual_add', views.virtual_add, name='virtual_add'),
path('virtual_delete', views.virtual_delete, name='virtual_delete'),
path('virtual_update', views.virtual_update, name='virtual_update'),


# XXX--END Virtual Section--XXX

# XXXX----admin_feedback------XXXXXXX
path('admin_feedback', views.admin_feedback, name='admin_feedback'),
path('feedback_delete', views.feedback_delete, name='feedback_delete'),
# XXXXXXX------END-----XXXXXXXXX

# XXXXXXXXX---START safety SECTION---XXXXXXXXXX
path('safety', views.safety, name='safety'),
path('safety_delete', views.safety_delete, name='safety_delete'),
path('safety_update', views.safety_update, name='safety_update'),
# XXXXXXXXX---END---XXXXXXXXXX

# XXXXXXXXX---START covid_state_link SECTION---XXXXXXXXXX
path('covid_state_link', views.covid_state_link, name='covid_state_link'),
path('covid_state_link_delete', views.covid_state_link_delete, name='covid_state_link_delete'),
path('covid_state_link_update', views.covid_state_link_update, name='covid_state_link_update'),
# XXX----END-----XXXX
]
