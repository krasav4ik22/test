import base64
import mimetypes
import os

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

def unvalidated_redirect(request):
    url = request.GET.get('url')
    return redirect(url)

