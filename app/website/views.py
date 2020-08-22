from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'web/base.html', {'title': "muskegg.com", 'description': "This is the index page. It's a Django app fully deployed automatically to a Kubernetes bare-metal cluster through a Jenkins declarative pipeline that builds, tags and pushes Docker images to a private registry. Everything is defined in a public GIT repo using git-secrets to hide sensitive information. The app (including the page you're reading right now) is reachable through an NGINX reverse proxy also automatically deployed through the same pipeline."})
