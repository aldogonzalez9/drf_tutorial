from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import renderers

from rest_framework.routers import DefaultRouter
from snippets import views 

# Create a router and register our views with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The apir URLs are now determined autmatically by the router
urlpatterns = [
    path('', include(router.urls))
]

#urlpatterns = format_suffix_patterns([urlpatterns])


