from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    footer_text = " "
    # Content for pipeline section
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
    # Content for 'raph' section
    section_raph_title = "About me"
    section_raph_intro = """I have been an IT professional for the best part of my life. I used to specialize in data storage technologies. From data recovery to data protection. Doing some electronics work on failed hard disk drive? Building ZFS storage arrays? Archive 15 years of M&E projects on LTO tapes? Been there, done that. Nowadays, I see myself as a Linux and Windows Systems Administrator. With a passion for automation and scripting, slowly getting more involved in anything DevOps.

    I’m currently living in Montreal and I’m working as a senior systems administrator for Moment Factory. I began working for Moment Factory back in 2014 as sysadmin and tech support. Supporting the 3D and content creation pipeline and managing the storage and archiving systems.

    I left the company in 2017 to go play with the much larger infrastructure at Framestore, an international VFX Studio as a senior sysadmin. I quickly became the “Dr. Storage” in the Montreal team, managing large storage buckets in various availability tiers. With the large render farm and the numerous servers we would provision and manage, I discovered the joys of configuration management even though we were using an outdated version of Puppet back then. Even if I always enjoyed working with Linux, the environment there being (almost) 100% Linux-based gave me the chance to largely improve my skills. Framestore also having studios all over the world (London, New York, Chicago, Los Angeles and Pune) connected through VPLS, it was the perfect playground to play with larger-scale networking, and switches and firewalls management.

    I heard the Moment Factory call once again in 2019 where I was hired in a more senior position where I could have a larger influence on projects and infrastructure’s development. I also had the opportunity to work on a huge client’s project as a DevOps support/consultant where we implemented an Ansible pipeline for the deployment of proprietary software and services. As everybody in IT knows, 2020 brought up great challenges for the development of networking and remote work. This gave me the opportunity to configure and tests many firewall and VPN products and get more experience with VMware’s software-defined networking solutions.
    """
    section_raph_muskeg_title = "muskeg"
    section_raph_muskeg = "The muskeg is where I grew up. It’s a type of terrain created by the accumulation of water and sediments on the near-surface bedrock preventing drainage. This type of terrain can be found all over Abitibi, my home region. I always loved the imagery of that rough terrain hard to navigate when you’re not used to it. About the improbable growth and hidden beauty amidst an hostile, acidic and almost permanently frozen environment."
    # Content dictionnary
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
        'section_raph_title': section_raph_title,
        'section_raph_intro': section_raph_intro,
        'section_raph_muskeg_title': section_raph_muskeg_title,
        'section_raph_muskeg': section_raph_muskeg,
        'footer_text': footer_text
    }
    return render(request, 'web/index.html', content)
