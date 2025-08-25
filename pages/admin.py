from django.contrib import admin
from .models import (
    Profile, Skill, Project, ProjectImage, Education, Experience, 
    Certification, Blog, Contact, SiteSettings
)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image', 'caption', 'is_primary', 'order']
    ordering = ['order']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email']
    fields = [
        'name', 'title', 'description', 'email', 'phone', 'location',
        'github_url', 'linkedin_url', 'twitter_url', 'resume_url', 'profile_image'
    ]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category', 'proficiency']
    list_editable = ['order']
    search_fields = ['name', 'category']
    ordering = ['category', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'date_created', 'order', 'get_image_count']
    list_filter = ['is_featured', 'date_created', 'technologies']
    list_editable = ['is_featured', 'order']
    search_fields = ['title', 'description']
    filter_horizontal = ['technologies']
    ordering = ['-is_featured', 'order', '-date_created']
    inlines = [ProjectImageInline]
    
    def get_image_count(self, obj):
        return obj.images.count()
    get_image_count.short_description = 'Images'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'short_description', 'description')
        }),
        ('Links & Demo', {
            'fields': ('github_url', 'demo_url')
        }),
        ('Classification', {
            'fields': ('technologies', 'is_featured', 'date_created', 'order')
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'start_date']
    search_fields = ['institution', 'degree', 'field_of_study']
    ordering = ['-start_date']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'experience_type', 'start_date', 'end_date', 'is_current']
    list_filter = ['experience_type', 'is_current', 'start_date']
    search_fields = ['title', 'organization', 'description']
    filter_horizontal = ['technologies_used']
    ordering = ['-start_date']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'issue_date', 'credential_id']
    list_filter = ['issuer', 'issue_date']
    search_fields = ['name', 'issuer', 'credential_id']
    filter_horizontal = ['skills']
    ordering = ['-issue_date']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'is_featured', 'medium_post_id']
    list_filter = ['is_featured', 'published_date']
    list_editable = ['is_featured']
    search_fields = ['title', 'description', 'tags']
    ordering = ['-published_date']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    list_editable = ['is_read']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_title']
    
    def has_add_permission(self, request):
        # Only allow one instance of SiteSettings
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of SiteSettings
        return False


# Customize admin site header
admin.site.site_header = "Biplove Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"
