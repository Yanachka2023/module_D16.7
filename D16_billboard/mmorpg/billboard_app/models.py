from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


tanks = "TA"
healers = "HE"
dd = "DD"
merchants = "ME"
guild_masters = "GM"
quest_givers = "QG"
blacksmiths = "BL"
tanners = "TA"
potion_makers = "PM"
spell_masters = "SM"


CATEGORIES = (
        (tanks, "Танки"),
        (healers, "Хилы"),
        (dd, "ДД"),
        (merchants, "Торговцы"),
        (guild_masters, "Гилдмастеры"),
        (quest_givers, "Квестгиверы"),
        (blacksmiths, "Кузнецы"),
        (tanners, "Кожевники"),
        (potion_makers, "Зельевары"),
        (spell_masters, "Мастера заклинаний")
    )





class Advertisement(models.Model):
    """Объявления"""
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=2, choices=CATEGORIES, default=quest_givers)
    upload = models.ImageField(blank=True, null=True, upload_to='content')
    subject = models.CharField("Тема", max_length=200)
    description = models.TextField("Объявление", max_length=10000)
    images = models.ForeignKey('gallery.Gallery',verbose_name="Изображения", blank=True, null=True,on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('advertisement_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

class  UserResponse(models.Model):
    """Отзовы"""
    commentator = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    text_of_response = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    subject = models.CharField("Тема", max_length=200)
    description = models.TextField("Объявление", max_length=10000)



    def get_absolute_url(self):
        return reverse('response_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Отзов"
        verbose_name_plural = "Отзовы"

# Create your models here.
