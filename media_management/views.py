from rest_framework.views import APIView, Response
from rest_framework.parsers import MultiPartParser, FormParser
from media_management .models import  Media
from media_management.serlizer import  MediaSerializer


class UploadMediaToLibaryAPI(APIView):
    def post(self, request):
        input_json = Response({})
        output_json = {}
    
        request.POST._mutable = True
        input_json_var = request
        json_function_output_var = UploadMediaToLibaryJson.upload_media_to_libary_json_function(self, input_json_var)
        output_json['Payload'] = json_function_output_var
        return Response(json_function_output_var)


class UploadMediaToLibaryJson(APIView):
    def upload_media_to_libary_json_function(self, request):
        input_json = (request.data).dict()
        
        # parser_classes = (MultiPartParser, FormParser)
        output_json = {}
        insert_api_params_var = {}
        try:
            if 'file_content' not in request.data:
                output_json['Status'] = "Failure"
                output_json['Message'] = "No files has been selected"
                output_json['media_details'] = {}
                return output_json
            medialist = dict((request.data).lists())['file_content']

            for media_list in medialist:
                insert_api_params_var['file_content'] = media_list
                insert_api_params_var['file_caption'] = input_json['file_caption']

                insert_api_params_var['status'] = 1
                insert_api_params_var['added_by'] = "admin"
                insert_api_params_var['last_modified_by'] = "admin"
                try:
                    media_serializer_var = MediaSerializer(data=insert_api_params_var)
                    if media_serializer_var.is_valid(raise_exception=True):
                        media_serializer_var.save()
                        output_json['Status'] = "Success"
                        output_json['Message'] = "File uploaded successfully"

                except Exception as ex:
                    output_json['Status'] = "Failure"
                    output_json['Message'] = "some internal issue.Exception encountered:"+str(ex)
                    output_json['media_details'] = {}
                    return output_json
            try:
                media_details_var = Media.objects.filter(file_content=input_json['file_content'],
                                                            status__exact=1)
                serialized_media_details_var = MediaSerializer(media_details_var, many=True)
                output_json['Status'] = "Success"
                output_json['Message'] = "successflly uploaded media to library."
                output_json["media_details"] = serialized_media_details_var.data

            except Exception as ex:
                output_json['Status'] = "Failure"
                output_json[
                    'Message'] = "some internal issue while inserting uploading  mediadetails.Exception encountered:"
                output_json['MediaDetails'] = {}
                return output_json
        except Exception as ex:
            output_json['Status'] = "Failure"
            output_json[
                'Message'] = "some internal issue while inserting uploading  mediadetails.Exception encountered:"+str(ex)
            output_json['MediaDetails'] = {}
            return output_json

        return output_json
