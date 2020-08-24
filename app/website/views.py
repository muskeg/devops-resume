from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    footer_text = " "
    section_title = "this website"
    section_text = """As I got more interested in DevOps, I decided to setup this website that would serve the double purpose of showing off some techniques and projects while effectively adding new tools to my skills set. My old portfolio was also over 10-year old and now largely irrelevant, it needed a refresh.
I ended up with this project: <span style="font-style: italic;">a Django project fully deployed automatically to a Kubernetes bare-metal cluster through a Jenkins declarative pipeline that builds, tags and pushes Docker images to a private registry. Everything is defined in a public GIT repo using git-secrets to hide sensitive information. The project (including this app page you're reading right now) is reachable through a NGINX reverse proxy also automatically deployed through the same pipeline</span>.
These lines, full of buzzwords, were originally some &quot;hello world&quot; I used while developping the project. I keep them here as a reminder of the work I've done since the beginning.
"""
    return render(request, 'web/index.html', {'section_title': section_title, 'section_text': section_text, 'footer_text': footer_text})
