from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    footer_text = " "
    section_pipeline_title = "this website"
    section_pipeline_intro = """As I got more interested in DevOps, I decided to setup this website that would serve the double purpose of showing off some techniques and projects while effectively adding new tools to my skills set. My old portfolio was also over 10-year old and now largely irrelevant, it needed a refresh.
    The idea:
    <div style="font-style: italic; font-size: smaller; width: 95%; margin: auto 2.5vh;">"A Django project fully deployed automatically to a Kubernetes bare-metal cluster through a Jenkins declarative pipeline that builds, tags and pushes Docker images to a private registry. Everything is defined in a public Git repo using git-secrets to hide sensitive information. The project (including this app page you're reading right now) is reachable through a NGINX reverse proxy also automatically deployed through the same pipeline."</div>
    These lines, full of buzzwords, were originally some &quot;hello world&quot; I used while developping the project. I keep them here as a reminder of the work I've done since the beginning.
    """
    section_pipeline_subtitle = "the pipeline"
    section_pipeline_pipeline = """The idea came from an interview question I had: “how would you handle the pipeline for the       development of a new feature?”. Ever since I got that question, I wanted to try and build the pipeline and see it work for real.
    You can find the whole project on Github: <a href="https://github.com/muskeg/muskegg-dot-com">https://github.com/muskeg/muskegg-dot-com</a>
    """
    section_pipeline_app_title = "the app"
    section_pipeline_app = """So instead of a “new feature” I created a simple Django project. I didn’t know much about Django at the time, but I like Python and thought it would be great to play with something new. At this time, the project has an admin interface app doing nothing and a website app which is the static page you’re seeing now.
    """
    section_pipeline_jenkins_title = "Jenkins"
    section_pipeline_jenkins = """I also wanted to experience more with declarative pipelines in Jenkins so I quickly setup a server to handle builds. Using Github’s webhooks, a commit will trigger a build. Jenkins will pull the code from Github and then use docker-compose to build the app’s images (the app, the database, and an NGINX reverse proxy). The plan is to use docker-compose to run the app and implement further testing in the future. But at the moment, I’m only validating that the Python code is properly linted with Flake8. Once the images are built, Jenkins tags them with a version tag before pushing them to a private Docker registry.
    """
    section_pipeline_deploy_title = "Deployment"
    section_pipeline_deploy = """Once the images are tagged and pushed, Jenkins tells my master Kubernetes node to update the Django app to the version it just built. The Kubernetes “cluster” is currently just 2 nodes running on Rancher’s k3s on servers I manage. Since the cluster is provisioned with Ansible, adding new nodes only takes a few minutes. Since the app is not running in a traditional cloud environment, I decided to use a self-provisioned public edge proxy that will forward all http traffic to the cluster.
    """
    content = {
        'section_pipeline_title': section_pipeline_title,
        'section_pipeline_intro': section_pipeline_intro,
        'section_pipeline_subtitle': section_pipeline_subtitle,
        'section_pipeline_pipeline': section_pipeline_pipeline,
        'section_pipeline_app_title': section_pipeline_app_title,
        'section_pipeline_app': section_pipeline_app,
        'section_pipeline_jenkins_title': section_pipeline_jenkins_title,
        'section_pipeline_jenkins': section_pipeline_jenkins,
        'section_pipeline_deploy_title': section_pipeline_deploy_title,
        'section_pipeline_deploy': section_pipeline_deploy,
        'footer_text': footer_text
    }
    return render(request, 'web/index.html', content)
