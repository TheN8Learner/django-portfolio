from django.contrib import admin
from .models import Project, Skill, ContactMessage
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech", "status", "is_featured", "created_at")
    search_fields = ("title", "description", "status")
    list_filter = ("status", )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "level")
    search_fields = ("title", "category", "level")
    list_filter = ("category", "level")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "created_at")
    list_filter = ("name", "created_at")