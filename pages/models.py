from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    resume_url = models.URLField(blank=True)
    profile_image = CloudinaryField('image', blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # e.g., 'Programming Languages', 'Frameworks', etc.
    proficiency = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert')
    ])
    icon = models.CharField(max_length=100, blank=True)  # CSS class or icon name
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} ({self.category})"
    
    class Meta:
        ordering = ['category', 'order']


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, help_text="Brief description for project cards")
    technologies = models.ManyToManyField(Skill, related_name='projects', blank=True)
    github_url = models.URLField(blank=True, help_text="GitHub repository URL")
    demo_url = models.URLField(blank=True, help_text="Demo URL (YouTube, Drive, or any other link)")
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    date_created = models.DateField()
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower numbers first)")
    
    def __str__(self):
        return self.title
    
    def get_primary_image(self):
        """Get the first image for display in cards"""
        first_image = self.images.filter(is_primary=True).first()
        if first_image:
            return first_image
        return self.images.first()
    
    class Meta:
        ordering = ['-is_featured', 'order', '-date_created']


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')
    caption = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False, help_text="Use as main image for project cards")
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.project.title} - Image {self.order}"
    
    class Meta:
        ordering = ['order']


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    activities = models.TextField(blank=True)
    grade = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"
    
    class Meta:
        ordering = ['-start_date']


class Experience(models.Model):
    EXPERIENCE_TYPES = [
        ('work', 'Work Experience'),
        ('volunteer', 'Volunteer Experience'),
        ('internship', 'Internship'),
        ('project', 'Project Experience'),
    ]
    
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPES)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Skill, blank=True)
    
    def __str__(self):
        return f"{self.title} at {self.organization}"
    
    class Meta:
        ordering = ['-start_date']


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    credential_id = models.CharField(max_length=200, blank=True)
    credential_url = models.URLField(blank=True)
    badge_image = CloudinaryField('image', blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.issuer}"
    
    class Meta:
        ordering = ['-issue_date']


class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    url = models.URLField()
    published_date = models.DateTimeField()
    image = CloudinaryField('image', blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True)  # Comma-separated tags
    is_featured = models.BooleanField(default=False)
    medium_post_id = models.CharField(max_length=100, blank=True)  # For Medium integration
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']


class SiteSettings(models.Model):
    site_title = models.CharField(max_length=100, default="Biplove Portfolio")
    site_description = models.TextField(default="Portfolio website")
    favicon = CloudinaryField('image', blank=True, null=True)
    logo = CloudinaryField('image', blank=True, null=True)
    footer_text = models.TextField(default="© 2024 Biplove Gautam. All rights reserved.")
    analytics_code = models.TextField(blank=True)
    
    def __str__(self):
        return "Site Settings"
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
