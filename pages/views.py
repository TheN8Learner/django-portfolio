from django.shortcuts import render,  get_object_or_404, redirect
from .models import Project, Skill, ContactMessage
from .forms import ContactForm

# Create your views here.
def home(request):
    profile = {
        "name": "Alpha Oumar Diallo",
        "role": "Développeur Django débutant",
        "intro": "Je construis des projets web avec Django pour apprendre et créer mon portfolio.",
        "location": "Sénégal",
        "email": "dalphaoumar210@gmail.com",
        "available": True,
    }

    featured_projects = Project.objects.filter(is_featured=True).order_by("-created_at")[:3]

    total_projects = Project.objects.count()

    skills = Skill.objects.all().order_by("title")[:5]

    return render(request, "pages/home.html", {
        "profile": profile,
        "featured_projects": featured_projects,
        "total_projects": total_projects,
        "skills": skills,
    })

def about(request):
    return render(request, 'pages/about.html')

def projects(request):
    project_list = Project.objects.all().order_by("-created_at")
    return render(request, 'pages/projects.html', {'projects': project_list})

def contact(request):
    return render(request, 'pages/contact.html')

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    return render(request, "pages/project_detail.html", {
        "project": project
    })

def skills(request):
    skills_List = Skill.objects.all().order_by("category", "title")
    return render(request, "pages/skills.html", {"skills": skills_List})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {
        "form": form,
    })

def contact_success(request):
    return render(request, "pages/contact_success.html")