from django.urls import path
from .views import(portfolio,about,projects,contacts,flexbox,calculator,website,flexboxadvance,SQL,video)

urlpatterns = [
	path('',portfolio,name = 'portfolio'),
	path('about/',about,name = 'about'),
	path('projects/',projects,name = 'projects'),
	path('contacts/',contacts,name = 'contacts'),
	path('projects/flexbox/',flexbox,name = 'flexbox'),
	path('projects/calculator/',calculator,name = 'calculator'),
	path('projects/website/',website,name = 'website'),
	path('projects/flexboxadvance/',flexboxadvance,name = 'flexboxadvance'),
	path('projects/SQL/',SQL,name = 'SQL'),
	path('projects/video/',video, name = 'video'),
]