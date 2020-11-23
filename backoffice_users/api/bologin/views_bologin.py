from django.shortcuts import render, redirect
from rest_framework.views import APIView
from backoffice_users.models import BOUser


class BOLogoutAPI(APIView):
    def get(self, request):
        if request.session.has_key('user_id'):
            del request.session['user_id']
        if request.session.has_key('user_email'):
            del request.session['user_email']
        return redirect('/BO/login/')


class BOLoginAPI(APIView):
    def get(self, request):
        if request.session.has_key('user_id') & request.session.has_key('user_email'):
            return redirect('/BO/list/')
        return render(request, 'bo_login.html', {})

    def post(self, request):
        output_json = {}
        try:
            if 'email' in request.POST and 'password' in request.POST:
                user_var = BOUser.objects.get(
                    email__exact=request.POST['email'], status=1)
                if user_var.email != request.POST['email']:
                    output_json['Status'] = 'Failure'
                    output_json['Message'] = 'Invalid User email'
                elif user_var.password != request.POST['password']:
                    output_json['Status'] = 'Failure'
                    output_json['Message'] = 'Wrong Password'
                else:
                    output_json['Status'] = 'Success'
                    output_json['Message'] = 'User Loged In'
                    request.session['user_id'] = user_var.bo_user_id
                    request.session['user_email'] = user_var.email
            else:
                output_json['Status'] = 'Failure'
                output_json['Message'] = 'Invalid api'
        except:
            output_json['Status'] = 'Failure'
            output_json['Message'] = 'Login unsuccessful'
        finally:
            if output_json['Status'] == 'Success':
                return redirect('/BO/list/')
            else:
                return render(request, 'bo_login.html', output_json)
