from django.shortcuts import render, redirect
from rest_framework.views import APIView


class FrontendNotFound404API(APIView):
    def get(self, request):
        return render(request, 'frontend_404.html')
