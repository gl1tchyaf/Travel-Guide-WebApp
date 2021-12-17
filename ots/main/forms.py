from django import forms
from . import models


class HotelReview(forms.ModelForm):
    class Meta:
        model = models.HotelReview
        fields = ['name', 'hotelName', 'review', 'rating']