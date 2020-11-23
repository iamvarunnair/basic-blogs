from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
class ParaGraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = '__all__'
class BlogToParagraphMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogToParagraphMapping
        fields = '__all__'
class MetaTagTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagType
        fields = '__all__'
class MetaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTag
        fields = '__all__'
class BlogToMetaTagMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogToMetaTagMapping
        fields = '__all__'

class ParagraphToMediaMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParagraphToMediaMapping
        fields = '__all__'
