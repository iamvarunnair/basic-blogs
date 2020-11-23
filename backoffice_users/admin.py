from django.contrib import admin
from .models import BOUser, BOUserStatus

# Register your models here.


class BOUserAdmin(admin.ModelAdmin):
    list_display = ('bo_user_id', 'email', 'password', 'status')


admin.site.register(BOUser, BOUserAdmin)
admin.site.register(BOUserStatus)
