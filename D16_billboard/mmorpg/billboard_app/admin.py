from django.contrib import admin
from .models import *


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """Объявления"""
    list_display = (
        "id",
        "subject",
        "author",
        "category",
        "time_in",
    )
    list_display_links = ("subject",)
    list_filter = ("author", "category")

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    """Отклики"""
    list_display = (
        "id",
        "commentator",
        "advertisement",
        "subject",
    )
    list_display_links = ("subject",)
    list_filter = ("commentator",)

# Register your models here.
