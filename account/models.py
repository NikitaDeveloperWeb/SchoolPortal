from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

 
# Модель профиля пользователя
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,verbose_name="Автор")
    first_name_p = models.CharField(max_length=200,verbose_name="Имя",)
    last_name_p = models.CharField(max_length=200,verbose_name="Фамилия")
    date_of_birth = models.DateField(blank=True, null=True,verbose_name="Дата рождения")
    photo = models.ImageField(null=True, upload_to='artucle_img',verbose_name="Аватар")

    def __str__(self):
        return 'Профиль для пользователя {}'.format(self.user.username)

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'

# Модель НОВОСТИ
class articles(models.Model):
    title = models.CharField(max_length=200,verbose_name="Заголовок")
    article = models.TextField(verbose_name="Статья")
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    photo = models.ImageField(null=True, upload_to='artucle_img',)
    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'статья'
        ordering = ['-published']

