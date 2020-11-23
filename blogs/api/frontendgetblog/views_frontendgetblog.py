from django.shortcuts import render, redirect
from rest_framework.views import APIView
from blogs.models import Blog, BlogToParagraphMapping, ParagraphToMediaMapping, BlogToMetaTagMapping
from django.db.models import F
from django.db.models import Prefetch
from django.core.serializers.json import DjangoJSONEncoder


class FrontendGetBlogAPI(APIView):
    def get(self, request, **kwargs):
        # output_json = {'blog_id': self.kwargs['blog_id']}
        output_json = {}
        try:
            blog_var = Blog.objects.filter(
                blog_id__exact=self.kwargs['blog_id']).values('blog_title').first()
            if blog_var == None:
                output_json['Status'] = 'Failure'
                output_json['Message'] = 'Blog not found.'
                output_json['Payload'] = None
            else:
                output_json['Payload'] = {}
                output_json['Payload']['blog_id'] = self.kwargs['blog_id']
                output_json['Payload']['blog_title'] = blog_var['blog_title']
                meida_mapping_query = ParagraphToMediaMapping.objects.select_related(
                    'media_id')
                blog_para_list = BlogToParagraphMapping.objects.filter(blog_id=self.kwargs['blog_id']).select_related('paragraph_id').prefetch_related(Prefetch(
                    'paragraph_id', meida_mapping_query)).annotate(id=F('paragraph_id'), body=F('paragraph_id__paragraph_body'), image=F('paragraph_id__paragraphtomediamapping__media_id__file_content')).values('id', 'body', 'image')
                if blog_para_list == None or blog_para_list == []:
                    output_json['Status'] = 'Failure'
                    output_json['Message'] = 'Blog not found.'
                    output_json['Payload'] = None
                else:
                    blog_meta_tags_list = BlogToMetaTagMapping.objects.filter(blog_id=self.kwargs['blog_id']).select_related('tag_id', 'type_id').annotate(tag_name=F('tag_id__type_id__type_name'), tag_name_value=F('tag_id__type_id__type_name_value'), tag_content=F('tag_id__content')).values(
                        'tag_name', 'tag_name_value', 'tag_content')
                    if blog_meta_tags_list == None or blog_meta_tags_list == []:
                        output_json['Status'] = 'Failure'
                        output_json['Message'] = 'Blog not found.'
                        output_json['Payload'] = None
                    else:
                        output_json['Status'] = 'Success'
                        output_json['Message'] = 'Blog found.'
                        output_json['Payload']['paragraphs'] = list(
                            blog_para_list)
                        output_json['Payload']['meta_tags'] = list(
                            blog_meta_tags_list)
        except:
            output_json['Status'] = 'Failure'
            output_json['Message'] = 'Error while fetching blog.'
            output_json['Payload'] = None
        finally:
            return render(request, 'frontend_getblog.html', output_json)
