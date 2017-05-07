from django.urls import reverse_lazy
import sendgrid
import os
from sendgrid.helpers.mail import *
from celery import shared_task
from youtube_to_mp3.settings import FROM_EMAIL, EMAIL_SUBJECT


@shared_task
def send_mail(from_email, to_email, subject, content):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    if not sg.apikey:
        raise ValueError('Could not find SENDGRID_API_KEY environment variable!')
    from_email = Email(from_email)
    to_email = Email(to_email)
    content = Content("text/plain", content)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
#    print(response.status_code)
#    print(response.body)
#    print(response.headers)


@shared_task
def prepare_and_send_mail(audio_file_id, current_domain, to_email):
        # Send email to user with download url
        song_url = current_domain + str(reverse_lazy('download_file', args=[audio_file_id]))

        send_mail.delay(from_email=FROM_EMAIL, to_email=to_email, subject=EMAIL_SUBJECT,
                  content='Eto ti q pesnichkata moi: {}'.format(song_url))
