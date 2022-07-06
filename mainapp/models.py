from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.IntegerField(default=0, verbose_name="Баланс")
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    def __str__(self):
        return f"{self.username}"


class Point(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, 
        primary_key=True, related_name='user_point', 
        verbose_name="Пользователь", 
        )
    click_count = models.SmallIntegerField(default=1, verbose_name="Счет нажатий")
    last_click_date = models.DateField(auto_now=True, verbose_name="Дата нажатия")
    
    class Meta:
        db_table = "point"
        verbose_name = "Балл"
        verbose_name_plural = "Баллы"
        