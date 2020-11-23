from django.contrib import admin
from .models import BlogStatus, ParagraphStatus, Blog, Paragraph, BlogToParagraphMappingStatus, BlogToParagraphMapping, MetaTagStatus, MetaTagType, MetaTag, BlogToMetaTagMappingStatus, BlogToMetaTagMapping, ParagraphToMediaMappingStatus, ParagraphToMediaMapping

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_id', 'blog_title', 'blog_status')


class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('paragraph_id', 'paragraph_body', 'status')


class MetaTagAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'type_id', 'content', 'status')


class MetaTagTypeAdmin(admin.ModelAdmin):
    list_display = ('type_id', 'type_name', 'type_name_value')


class BlogToParagraphMappingAdmin(admin.ModelAdmin):
    list_display = ('map_id', 'blog_id', 'paragraph_id', 'status')


class BlogToMetaTagMappingAdmin(admin.ModelAdmin):
    list_display = ('blog_to_meta_tag_map_id', 'blog_id', 'tag_id', 'status')


class ParagraphToMediaMappingAdmin(admin.ModelAdmin):
    list_display = ('paragraph_to_media_map_id',
                    'paragraph_id', 'media_id')


admin.site.register(BlogStatus)
admin.site.register(ParagraphStatus)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(BlogToParagraphMappingStatus)
admin.site.register(BlogToParagraphMapping, BlogToParagraphMappingAdmin)
admin.site.register(MetaTagStatus)
admin.site.register(MetaTagType, MetaTagTypeAdmin)
admin.site.register(MetaTag, MetaTagAdmin)
admin.site.register(BlogToMetaTagMappingStatus)
admin.site.register(BlogToMetaTagMapping, BlogToMetaTagMappingAdmin)
admin.site.register(ParagraphToMediaMappingStatus)
admin.site.register(ParagraphToMediaMapping, ParagraphToMediaMappingAdmin)
