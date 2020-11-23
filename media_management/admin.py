from django.contrib import admin
from .models import Media, MediaStatus

# Register your models here.


class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_id', 'file_content', 'status')


admin.site.register(MediaStatus)
admin.site.register(Media, MediaAdmin)
