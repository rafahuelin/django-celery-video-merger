from django.urls import path
# from django.views.generic import TemplateView

from . import views

app_name = 'video_merger'

urlpatterns = [
    # path('', TemplateView.as_view(template_name="video_merger/home.html"), name="home"),
    path('', views.VideosUploadView.as_view(), name="upload"),
]
