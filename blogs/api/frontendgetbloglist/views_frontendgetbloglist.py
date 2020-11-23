from django.shortcuts import render, redirect
from rest_framework.views import APIView
from blogs.models import Blog, BlogToParagraphMapping, ParagraphToMediaMapping
from django.core.serializers.json import DjangoJSONEncoder
import json


class FrontendGetBlogListAPI(APIView):
    def get(self, request):
        output_json = {}
        try:
            blogs_var = Blog.objects.filter(
                blog_status=1).values('blog_id', 'blog_title')
            if blogs_var == None:
                output_json['Status'] = 'Failure'
                output_json['Message'] = 'No blog entries at the moment.'
                output_json['Payload'] = None
            else:
                for index in blogs_var:
                    blog_para_var = BlogToParagraphMapping.objects.filter(blog_id=index['blog_id']).select_related(
                        'paragraph_id').values('paragraph_id', 'paragraph_id__paragraph_body').first()
                    if blog_para_var != None:
                        index['blog_body'] = blog_para_var['paragraph_id__paragraph_body']
                        blog_image_var = ParagraphToMediaMapping.objects.filter(
                            paragraph_id=blog_para_var['paragraph_id']).select_related('media_id').values('media_id__file_content').first()
                        if blog_image_var != None:
                            index['blog_image'] = blog_image_var['media_id__file_content']
                        else:
                            index['blog_image'] = None
                    else:
                        index['blog_body'] = None
                output_json['Payload'] = json.dumps(
                    {"blog_list": list(blogs_var)}, cls=DjangoJSONEncoder)
        except:
            output_json['Status'] = 'Failure'
            output_json['Message'] = 'Error occured while fetching blog details.'
            output_json['Payload'] = None
        finally:
            return render(request, 'frontend_getbloglist.html', output_json)
