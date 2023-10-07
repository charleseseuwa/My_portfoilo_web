from django.urls import path
from .views import index_page, contact_page, successView



urlpatterns = [
    path('',index_page, name='index'),
    path('contact/',contact_page, name='contact'),
    path("success/", successView, name="success")
]
