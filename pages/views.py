from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from .models import (
    Profile, Skill, Project, Education, Experience, 
    Certification, Blog, Contact, SiteSettings
)
from .utils import auto_sync_medium_blogs


def index(request):
    """Homepage view with limited content and featured items"""
    try:
        # Auto-sync Medium blogs (you might want to do this periodically instead)
        auto_sync_medium_blogs()
    except Exception as e:
        print(f"Error syncing Medium blogs: {str(e)}")
    
    # Get profile data
    profile = Profile.objects.first()
    
    # Get featured/limited content for homepage
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    all_skills = Skill.objects.all()
    recent_education = Education.objects.all()[:2]
    recent_experience = Experience.objects.all()[:3]
    recent_certifications = Certification.objects.all()[:3]
    featured_blogs = Blog.objects.filter(is_featured=True)[:3]
    
    # Group skills by category
    skills_by_category = {}
    for skill in all_skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'skills_by_category': skills_by_category,
        'education': recent_education,
        'experience': recent_experience,
        'certifications': recent_certifications,
        'featured_blogs': featured_blogs,
    }
    return render(request, 'index.html', context)


def about(request):
    """About page with full profile information"""
    profile = Profile.objects.first()
    all_education = Education.objects.all()
    all_experience = Experience.objects.all()
    all_certifications = Certification.objects.all()
    all_skills = Skill.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for skill in all_skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context = {
        'profile': profile,
        'education': all_education,
        'experience': all_experience,
        'certifications': all_certifications,
        'skills_by_category': skills_by_category,
    }
    return render(request, 'about.html', context)


def projects(request):
    """Projects page with all projects"""
    all_projects = Project.objects.all()
    
    # Pagination
    paginator = Paginator(all_projects, 6)  # Show 6 projects per page
    page_number = request.GET.get('page')
    projects_page = paginator.get_page(page_number)
    
    context = {
        'projects': projects_page,
        'total_projects': all_projects.count(),
    }
    return render(request, 'projects.html', context)


def blogs(request):
    """Blogs page with all blog posts"""
    all_blogs = Blog.objects.all()
    
    # Pagination
    paginator = Paginator(all_blogs, 6)  # Show 6 blogs per page
    page_number = request.GET.get('page')
    blogs_page = paginator.get_page(page_number)
    
    context = {
        'blogs': blogs_page,
        'total_blogs': all_blogs.count(),
    }
    return render(request, 'blogs.html', context)


def project_detail(request, project_id):
    """Individual project detail page"""
    project = get_object_or_404(Project, id=project_id)
    related_projects = Project.objects.exclude(id=project_id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'project_detail.html', context)


def contact(request):
    """Contact page and form handling"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if all([name, email, subject, message]):
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'contact.html', context)


def sync_medium_blogs(request):
    """Manual sync of Medium blogs (AJAX endpoint)"""
    if request.method == 'POST' and request.user.is_staff:
        success, message = auto_sync_medium_blogs()
        return JsonResponse({
            'success': success,
            'message': message
        })
    return JsonResponse({'success': False, 'message': 'Unauthorized'})


def services(request):
    """Services page - keeping the sorry page for now"""
    return render(request, 'sorry.html')


def error_404(request, exception):
    """Custom 404 error page"""
    return render(request, '404.html', status=404)


def error_500(request):
    """Custom 500 error page"""
    return render(request, '500.html', status=500)
    return render(request, 'sorry.html', status=404)
