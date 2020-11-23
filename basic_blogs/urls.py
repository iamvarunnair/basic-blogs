"""basic_blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from blogs.api.frontendgetbloglist.views_frontendgetbloglist import FrontendGetBlogListAPI
from blogs.api.frontendgetblog.views_frontendgetblog import FrontendGetBlogAPI
from blogs.api.frontendnotfound404.views_frontendnotfound404 import FrontendNotFound404API
from blogs.api.boaddblog.views_boaddblog import BOAddBlogAPI
from blogs.api.bogetbloglist.views_bogetbloglist import BOGetBlogListAPI
from blogs.api.boremoveblog.views_boremoveblog import BORemoveBlogAPI
from backoffice_users.api.bologin.views_bologin import BOLoginAPI, BOLogoutAPI
from media_management.views import UploadMediaToLibaryAPI
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^list/$', FrontendGetBlogListAPI.as_view(), name="frontend_getbloglist"),
    url(r'^view/(?P<blog_id>[0-9]+)$',
        FrontendGetBlogAPI.as_view(), name="frontend_getblog"),
    url(r'^404/$',
        FrontendNotFound404API.as_view(), name="frontend_not_found_404"),
    url(r'^BO/addBlog/$', BOAddBlogAPI.as_view(), name="bo_add_blog"),
    url(r'^BO/removeBlog/$', BORemoveBlogAPI.as_view(), name="bo_remove_blog"),
    url(r'^BO/list/$', BOGetBlogListAPI.as_view(), name="bo_get_blog_list"),
    url(r'^BO/login/$', BOLoginAPI.as_view(), name="bo_login"),
    url(r'^BO/logout/$', BOLogoutAPI.as_view(), name="bo_logout"),
    url(r'^BO/$', RedirectView.as_view(pattern_name="bo_get_blog_list")),
    url(r'^uploadMediaToLibary/$',
        UploadMediaToLibaryAPI.as_view(), name="upload_media"),
    url(r'^$', RedirectView.as_view(pattern_name="frontend_getbloglist"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
