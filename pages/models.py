from django.db import models

# Create your models here.

class Project(models.Model):
    STATUS_CHOICES = [
        ("planned", "Prévu"),
        ("in_progress", "En cours"),
        ("completed", "Terminé"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    tech = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="planned"
    )
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    CategoryChoices = [
        ("Fontend", "Fontend"),
        ("Backend", "Backend"),
        ("General", "General"),
    ]

    LevelChoices = [
        ("beginner", "Débutant"),
        ("intermediate", "Intermediaire"),
        ("advanced", "Avancé")
    ]
    


    title= models.CharField(max_length=200)
    category= models.CharField(
        max_length=200,
        choices=CategoryChoices,
        default="General")
    level= models.CharField(
        max_length=200, 
        choices=LevelChoices, 
        default="Débutant")


    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.name}"