from django.views.generic.edit import FormView

from .forms import VideosUploadForm
from .utils import create_destination_folder, merge_videos, upload_original_videos


class VideosUploadView(FormView):
    form_class = VideosUploadForm
    template_name = 'video_merger/upload.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        videos = request.FILES.getlist('file_field')
        if form.is_valid():
            destination_folder = create_destination_folder()
            for video_number, video in enumerate(videos, 1):
                upload_original_videos(video, video_number, destination_folder)
            merge_videos(destination_folder)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
