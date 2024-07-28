from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Advertisement, UserResponse


class AdvertisementFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='time_in',
        lookup_expr='lt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
       model = Advertisement
       fields = {
           'heading': ['icontains'],
           'category': ['exact'],
           'author': ['exact']
       }


class UserResponseFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='time_in',
        lookup_expr='lt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
       model = UserResponse
       fields = {
           'commentator': ['exact'],
           'advertisement': ['exact']
       }