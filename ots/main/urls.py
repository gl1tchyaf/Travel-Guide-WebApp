from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'articles'


urlpatterns = [
    url(r'^$', views.homepage, name="list"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^ticket/$', views.ticket, name="ticket"),
    url(r'^ticket_page/$', views.ticket_page, name="ticket_page"),
    url(r'^hotel_booking/$', views.hotel_booking, name="hotel_booking"),
    url(r'^hotelReview/$', views.hotelReview, name="hotelReview"),
    url(r'^hotelReviewShow/$', views.hotelReviewShow, name="hotelReviewShow"),
    path('deleteHotelReview/<str:pk>/$', views.deleteHotelReview, name="deleteHotelReview"),

]
