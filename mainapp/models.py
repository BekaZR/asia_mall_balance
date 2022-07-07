import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    balance = models.IntegerField(default=0, verbose_name="Баланс")
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    def __str__(self):
        return f"{self.username}"


class Point(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, 
        related_name='user_point', 
        verbose_name="Пользователь", 
        )
    click_count = models.SmallIntegerField(default=1, verbose_name="Счет нажатий")
    last_click_date = models.DateField(auto_now=True, verbose_name="Дата нажатия")
    
    class Meta:
        db_table = "point"
        verbose_name = "Балл"
        verbose_name_plural = "Баллы"
    
    @property
    def default_value_click_count(self):
        self.click_count = 1
        return self.save()
    
    @property
    def add_click_count_from_instance(self):
        self.click_count += 1
        return self.save()
    
    @property
    def add_from_user_balance(self):
        self.user.balance += self.click_count
        return self.user.save()
    
    


@receiver(post_save, sender=User)
def create_connected_models(sender, instance, created, **kwargs):
    if created:
        Point.objects.create(user=instance)