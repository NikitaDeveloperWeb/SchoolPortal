from django.contrib import admin
from .models import Profile,articles

# Отображение профиля в cms
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo','first_name_p','last_name_p']
    
# Отображение сообщений в cms
class MessageAdmin(admin.ModelAdmin):
    exclude = ('author',)
    list_display = ['autor','title','article','photo']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(articles)   