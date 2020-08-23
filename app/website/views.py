from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    section-title = "this website"
    description = "This website is a Django project fully deployed automatically to a Kubernetes bare-metal cluster through a Jenkins declarative pipeline that builds, tags and pushes Docker images to a private registry. Everything is defined in a public GIT repo using git-secrets to hide sensitive information. The project (including this app page you're reading right now) is reachable through an NGINX reverse proxy also automatically deployed through the same pipeline."
    return render(request, 'web/index.html', {'title': section-title, 'description': description})
