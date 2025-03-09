from django.contrib import admin
from.models import mail

# Register your models here.





class admin_mail(admin.ModelAdmin):
    list_display = ('name', 'created_at')



admin.site.register(mail, admin_mail)
