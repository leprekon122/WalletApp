from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve
from django.urls import path
from . import views

urlpatterns = [
   path('', views.login_page, name='login_page'),
   path('main_page', views.MainPage.as_view(), name='main_page')

]

urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
    ]