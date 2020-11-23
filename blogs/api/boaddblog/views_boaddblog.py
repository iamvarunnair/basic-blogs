from rest_framework.views import APIView, Response
from django.shortcuts import render, redirect
from blogs.serializers import BlogSerializer, ParaGraphSerializer, BlogToParagraphMappingSerializer, \
    MetaTagSerializer, BlogToMetaTagMappingSerializer, ParagraphToMediaMappingSerializer
from media_management.serlizer import MediaSerializer
from blogs.models import MetaTagType
from django.core.serializers.json import DjangoJSONEncoder
import json


class BOAddBlogAPI(APIView):
    def get(self, request):
        if request.session.has_key('user_id') & request.session.has_key('user_email'):
            output_json = {}
            output_json['Payload'] = {}
            try:
                meta_tag_type_list = MetaTagType.objects.all().values(
                    'type_id', 'type_name', 'type_name_value')
                if meta_tag_type_list != None:
                    output_json['Status'] = 'Success'
                    output_json['Message'] = 'Successfully page fetched.'
                    output_json['Payload']['meta_tag_type_list'] = list(
                        meta_tag_type_list)
                    output_json['Payload']['json_string'] = json.dumps({
                        "meta_tag_type_list": list(meta_tag_type_list)}, cls=DjangoJSONEncoder)
                else:
                    output_json['Status'] = 'Failure'
                    output_json['Message'] = 'Couldn\'t load necessary data to display page.'
                    output_json['Payload']['meta_tag_type_list'] = None
            except:
                output_json['Status'] = 'Failure'
                output_json['Message'] = 'Couldn\'t display page.'
                output_json['Payload']['meta_tag_type_list'] = None
            finally:
                return render(request, 'bo_addblog.html', output_json)
        return redirect('/BO/login/')

    def post(self, request):
        if request.session.has_key('user_id') & request.session.has_key('user_email'):
            output_json = {}
            input_json = {'blog_title': request.POST.get(
                'blog_title'), 'paragraph_list': [], 'meta_tag_list': []}
            request.POST._mutable = True
            paragraph_counter = 1
            meta_tag_counter = 1

            index = 1
            while ('paragraph' + str(index) in request.POST and 'file_content' + str(index) in request.FILES)\
                    or ('tag_type' + str(index) in request.POST and 'tag_content' + str(index) in request.POST):
                if 'paragraph' + str(index) in request.POST and 'file_content' + str(index) in request.FILES:
                    input_json['paragraph_list'].append({
                        'paragraph_body': request.POST['paragraph'+str(index)],
                        'file_content': request.FILES['file_content'+str(index)]
                    })
                if 'tag_type' + str(index) in request.POST and 'tag_content' + str(index) in request.POST:
                    input_json['meta_tag_list'].append({
                        'type_id': request.POST['tag_type' + str(index)],
                        'tag_content': request.POST['tag_content' + str(index)]
                    })
                index = index + 1

            json_function_output_var = BOAddBlogJson.bo_add_blog_json_function(
                input_json)
            output_json = json_function_output_var
            output_json['Payload'] = {}
            output_json['Payload']['redirect_url'] = 'bo_add_blog'
            output_json['Payload']['redirect_button'] = 'Add Another blog'
            return render(request, 'response_message.html', output_json)
        return redirect('/BO/login/')


class BOAddBlogJson:
    @staticmethod
    def bo_add_blog_json_function(request):
        # parser_classes = (MultiPartParser, FormParser)
        input_json = request
        output_json = {}
        try:
            # ###### insert into blog ######
            add_blog_param_var = {'blog_title': input_json['blog_title'], 'blog_status': 1,
                                  'added_by': str(input_json['blog_title']), 'last_modified_by': str(
                input_json['blog_title'])}

            blog_serializer_var = BlogSerializer(
                data=add_blog_param_var)
            if blog_serializer_var.is_valid(raise_exception=True):
                blog_serializer_var.save()

                # ###### insert into meta tag ######
                meta_tag_list = []
                for x in input_json['meta_tag_list']:
                    meta_tag_list.append({
                        'type_id': x['type_id'],
                        'content': x['tag_content'],
                        'added_by': 'admin',
                        'last_modified_by': 'admin',
                        'status': 1
                    })

                meta_tag_serializer_var = MetaTagSerializer(
                    data=meta_tag_list, many=True)
                if meta_tag_serializer_var.is_valid(raise_exception=True):
                    inserted_meta_tag_list = meta_tag_serializer_var.save()

                    # ###### insert into blog to meta tag mapping (one to many) ######
                    blog_to_meta_tag_map_params_var = []
                    for i in inserted_meta_tag_list:
                        blog_to_meta_tag_map_params_var.append({
                            'blog_id': blog_serializer_var.data['blog_id'],
                            'tag_id': i.tag_id,
                            'status': 1,
                            'added_by': str(input_json['blog_title']),
                            'last_modified_by': str(input_json['blog_title'])})

                    blog_to_meta_tag_map_serializer_var = BlogToMetaTagMappingSerializer(
                        data=blog_to_meta_tag_map_params_var, many=True)
                    if blog_to_meta_tag_map_serializer_var.is_valid(raise_exception=True):
                        blog_to_meta_tag_map_serializer_var.save()

                # ###### insert into paragraphs ######
                paragraph_list = []
                for x in input_json['paragraph_list']:
                    paragraph_list.append({
                        'paragraph_body': x['paragraph_body'],
                        'added_by': 'admin',
                        'last_modified_by': 'admin',
                        'status': 1,
                    })

                add_paragraph_serializer_var = ParaGraphSerializer(
                    data=paragraph_list, many=True)
                if add_paragraph_serializer_var.is_valid(raise_exception=True):
                    inserted_paragraph_list = add_paragraph_serializer_var.save()

                    # ###### insert into blog to paragraph mapping (one to many) ######
                    blog_to_paragraph_map_params_var = []
                    for i in inserted_paragraph_list:
                        blog_to_paragraph_map_params_var.append({
                            'blog_id': blog_serializer_var.data['blog_id'],
                            'paragraph_id': i.paragraph_id,
                            'status': 1, 'added_by': str(input_json['blog_title']),
                            'last_modified_by': str(input_json['blog_title'])})

                    blog_to_paragraph_map_serializer_var = BlogToParagraphMappingSerializer(
                        data=blog_to_paragraph_map_params_var, many=True)
                    if blog_to_paragraph_map_serializer_var.is_valid(raise_exception=True):
                        blog_to_paragraph_map_serializer_var.save()

                        # ###### insert into media ######
                        media_list = []
                        for x in input_json['paragraph_list']:
                            media_list.append({
                                'file_content': x['file_content'],
                                'file_caption': 'image',
                                'added_by': 'admin',
                                'last_modified_by': 'admin',
                                'status': 1
                            })

                        media_id_serializer_var = MediaSerializer(
                            data=media_list, many=True)
                        if media_id_serializer_var.is_valid(raise_exception=True):
                            media_id_list = media_id_serializer_var.save()

                            # ###### insert into paragraph to media mapping (one to many) ######
                            paragraph_to_media_map_params_var = []
                            j = 0
                            for i in media_id_list:
                                paragraph_to_media_map_params_var.append({
                                    'paragraph_id': inserted_paragraph_list[j].paragraph_id,
                                    'media_id': i.media_id,
                                    'status': 1,
                                    'added_by': str(input_json['blog_title']),
                                    'last_modified_by': str(input_json['blog_title'])})
                                j = j+1

                            paragraph_to_media_map_serializer_var = ParagraphToMediaMappingSerializer(
                                data=paragraph_to_media_map_params_var, many=True)
                            if paragraph_to_media_map_serializer_var.is_valid(raise_exception=True):
                                paragraph_to_media_map_serializer_var.save()

                output_json['Status'] = "Success"
                output_json['Message'] = "Successfully added blog."
                return output_json

        except Exception as ex:
            output_json['Status'] = "Failure"
            output_json['Message'] = " Some internal issue blog not created successfully.Exception encountered: " + \
                                     str(ex)
            return output_json
