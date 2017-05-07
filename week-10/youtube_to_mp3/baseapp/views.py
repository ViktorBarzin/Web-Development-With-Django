import mimetypes
import os
from django.http import HttpResponseBadRequest, StreamingHttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from wsgiref.util import FileWrapper

# Create your views here.
from .forms import VideoInputForm
from .models import AudioFile
from .tasks import create_mp3_object_and_return_obj_id
from converter.tasks import convert_to_mp3
from downloader.tasks import download_video
from emailer.tasks import prepare_and_send_mail
from youtube_to_mp3.settings import DOWNLOAD_VIDEO_PATH


def index_view(request):
    # TODO: add quality options in download menu? maybe in template?
    form = VideoInputForm()
    if request.method == 'POST':
        form = VideoInputForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            to_email = form.cleaned_data.get('email')
        else:
            return HttpResponseBadRequest('<h1>Bad request!<br /> Don\'t play smartass...</h1>')

        # Touching any of the chained method interfaces will break the chain.
        # So don't even think about it!
        chain = (download_video.s(url=url, file_path=DOWNLOAD_VIDEO_PATH)
                | convert_to_mp3.s()
                | create_mp3_object_and_return_obj_id.s()
                | prepare_and_send_mail.s(request.get_host(), to_email))
        chain.apply_async()
        return redirect(reverse_lazy('thankyou'))
    return render(request, 'index.html', locals())


def thankyou_view(request):
    return render(request, 'thank_you.html', locals())


def download_file_view(request, pk):
    '''
    This view displays the converted video as mp3 and offers
    the option to download it.
    '''
    audio_file = get_object_or_404(AudioFile, id=pk)

    filename = str(audio_file)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(str(audio_file.file_path), 'rb'), chunk_size),
                                     content_type=mimetypes.guess_type(str(audio_file.file_path))[0])
    response['Content-Length'] = os.path.getsize(str(audio_file.file_path))
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
