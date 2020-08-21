from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("This is the index page. It's fully deployed automatically to kubernetes through a Jenkins pipeline building and pushing docker images to a private registry, as defined in git repo, using an NGINX reverse proxy to show you that page.")
