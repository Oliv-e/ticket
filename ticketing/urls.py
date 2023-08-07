"""
URL configuration for ticketing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from App import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    # Home
    path('', views.home, name="home"),
    # EO DATA
    path('data_eo', views.data_eo, name="data_eo"),
    # Add EventOrganizer
    path('add_eventorganizer', views.add_eo, name="add_eo"),
    # View Data EO
    path('eventorganizer/<str:eo_id>', views.eo, name="eo"),
    # Edit Data EO
    path('edit_eventorganizer', views.edit_eo, name="edit_eo"),
    # Delete EO
    path('delete_eventorganizer/<str:eo_id>', views.delete_eo, name="delete_eo"),
    # Event Data
    path('data_event', views.data_event, name="data_event"),
    # Add Event
    path('add_event', views.add_event, name="add_event"),
    # View Data Event
    path('event/<str:event_id>',views.event,name="event"),
    # Edit Data Event
    path('edit_event',views.edit_event, name="edit_event"),
    # Delete Data Event
    path('delete_event/<str:event_id>',views.delete_event, name="delete_event")
]