from rest_framework.views import APIView, Response
from django.shortcuts import render, redirect
from blogs.models import Blog, BlogToParagraphMapping, Paragraph, ParagraphToMediaMapping, BlogToMetaTagMapping, MetaTag
from media_management.models import Media
from django.db.models import OuterRef, Subquery


class BORemoveBlogAPI(APIView):
    def post(self, request):
        if request.session.has_key('user_id') & request.session.has_key('user_email'):
            output_json = {}
            import pdb
            pdb.set_trace()
            if 'blog_id' in request.POST:
                input_json = {'blog_id': request.POST['blog_id']}
                output_json = BORemoveBlogJson.bo_remove_blog_json(input_json)
            else:
                output_json['Status'] = 'Failure'
                output_json['Message'] = 'Couldn\'t identify the blog to be removed.'

            output_json['Payload'] = {}
            output_json['Payload']['redirect_url'] = 'bo_add_blog'
            output_json['Payload']['redirect_button'] = 'Add Another blog'

            return render(request, 'response_message.html', output_json)
        return redirect('/BO/login/')


class BORemoveBlogJson:
    @staticmethod
    def bo_remove_blog_json(request):
        input_json = request
        output_json = {}
        try:
            Blog.objects.filter(
                blog_id__exact=input_json['blog_id'], blog_status=1).update(blog_status=2)

            blog_to_meta_tag_mapping_query = BlogToMetaTagMapping.objects.filter(
                blog_id=input_json['blog_id'], status=1)
            meta_tag_query = MetaTag.objects.filter(tag_id__in=Subquery(
                blog_to_meta_tag_mapping_query.values('tag_id')), status=1)

            meta_tag_query.update(status=2)
            blog_to_meta_tag_mapping_query.update(status=2)

            blog_to_para_mapping_query = BlogToParagraphMapping.objects.filter(
                blog_id=input_json['blog_id'], status=1)
            paragraph_query = Paragraph.objects.filter(paragraph_id__in=Subquery(
                blog_to_para_mapping_query.values('paragraph_id')), status=1)
            para_to_media_mapping_query = ParagraphToMediaMapping.objects.filter(
                paragraph_id__in=paragraph_query.values('paragraph_id'), status=1)
            media_query = Media.objects.filter(media_id__in=Subquery(
                para_to_media_mapping_query.values('media_id')))

            media_query.update(status=2)
            para_to_media_mapping_query.update(status=2)
            paragraph_query.update(status=2)
            blog_to_para_mapping_query.update(status=2)

            output_json['Status'] = 'Success'
            output_json['Message'] = 'Blog and related data successfully removed.'
        except:
            output_json['Status'] = 'Failure'
            output_json['Message'] = 'Couldn\'t remove blog.'
        finally:
            return output_json
