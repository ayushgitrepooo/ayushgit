from django.contrib import admin
from .models import Project, Skill,  Experience, Education, Contact

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'project_url', 'github_link']
    search_fields = ['title', 'technologies']
    list_filter = ['technologies']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency']
    search_fields = ['name',]
    list_filter = ['proficiency',]
    
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'role', 'start_date', 'end_date']
    search_fields = ['company', 'role']
    list_filter = ['start_date', 'end_date']
    
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'complete_year']     
    search_fields = ['degree', 'institution']
    list_filter = ['complete_year']   
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_no']
    search_fields = ['email', 'phone_no']    
    
    
    