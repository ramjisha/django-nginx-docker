from django.http import HttpResponse
import datetime

def now(request):

    now = datetime.datetime.now() 

    msg = f'Today is {now}'

    return HttpResponse(msg, content_type='text/plain')