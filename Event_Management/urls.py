"""
URL configuration for Event_Management project.

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
from django.urls import path
from event_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup,name='signup'),
    path('signin/', views.signin, name='signin'),
    path('about/',views.about,name='about'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('feed/',views.feed,name='feed'),
    path('booking/', views.booking, name='booking'),
    path('booking1/', views.booking1, name='booking1'),
    path('booking2/', views.booking2, name='booking2'),
    path('booking3/', views.booking3, name='booking3'),
    path('booking4/', views.booking4, name='booking4'),
    path('booking5/', views.booking5, name='booking5'),
    path('booking6/', views.booking6, name='booking6'),
    path('booking7/', views.booking7, name='booking7'),
    path('feedback_Data',views.feedback_Data,name='submit_f'),
    path('my_registrations/',views.my_registrations, name='myrgs'),
    path('submit_booking/', views.submit_booking, name='submit_booking'),
    path('submit_booking1/', views.submit_booking1, name='submit_booking1'),
    path('submit_booking2/', views.submit_booking2, name='submit_booking2'),
    path('submit_booking3/', views.submit_booking3, name='submit_booking3'),
    path('submit_booking4/', views.submit_booking4, name='submit_booking4'),
    path('submit_booking5/', views.submit_booking5, name='submit_booking5'),
    path('submit_booking6/', views.submit_booking6, name='submit_booking6'),
    path('submit_booking7/', views.submit_booking7, name='submit_booking7'),
    path('deleteData/<int:id>',views.deleteData,name='deleteData'),
    path('updateBooking/<int:id>/', views.updateData, name='updateData'),
    path('signout/',views.signout,name='signout'),
    
]
