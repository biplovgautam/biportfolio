from django.core.management.base import BaseCommand
from django.utils import timezone
from pages.models import (
    Profile, Skill, Project, Education, Experience, 
    Certification, Blog, Contact, SiteSettings
)
from datetime import date


class Command(BaseCommand):
    help = 'Populate initial data based on user requirements'

    def handle(self, *args, **options):
        self.stdout.write('Populating initial data...')
        
        # Create Profile
        profile, created = Profile.objects.get_or_create(
            defaults={
                'name': 'Biplove Gautam',
                'title': 'Computer Science Student & AI Enthusiast',
                'description': 'Passionate Computer Science student specializing in Artificial Intelligence and Machine Learning. Currently pursuing BSc. (Hons) in Computer Science with AI at Coventry University.',
                'email': 'biplove@example.com',
                'phone': '+977-XXXXXXXXX',
                'location': 'Nepal',
                'github_url': 'https://github.com/biplovgautam',
                'linkedin_url': 'https://linkedin.com/in/biplovgautam',
            }
        )
        if created:
            self.stdout.write(f'Created profile for {profile.name}')

        # Create Skills
        skills_data = [
            {'name': 'Python', 'category': 'Programming Languages', 'proficiency': 'advanced'},
            {'name': 'JavaScript', 'category': 'Programming Languages', 'proficiency': 'intermediate'},
            {'name': 'HTML/CSS', 'category': 'Web Technologies', 'proficiency': 'advanced'},
            {'name': 'Django', 'category': 'Frameworks', 'proficiency': 'intermediate'},
            {'name': 'React', 'category': 'Frameworks', 'proficiency': 'intermediate'},
            {'name': 'PyTorch', 'category': 'AI/ML', 'proficiency': 'intermediate'},
            {'name': 'OpenCV', 'category': 'AI/ML', 'proficiency': 'intermediate'},
            {'name': 'Git', 'category': 'Tools', 'proficiency': 'advanced'},
            {'name': 'GitHub', 'category': 'Tools', 'proficiency': 'advanced'},
            {'name': 'Machine Learning', 'category': 'AI/ML', 'proficiency': 'intermediate'},
            {'name': 'Deep Learning', 'category': 'AI/ML', 'proficiency': 'intermediate'},
            {'name': 'Computer Vision', 'category': 'AI/ML', 'proficiency': 'intermediate'},
            {'name': 'RAG', 'category': 'AI/ML', 'proficiency': 'beginner'},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')

        # Create Education
        education_data = [
            {
                'institution': 'Coventry University',
                'degree': 'BSc. (Hons) in Computer Science with Artificial Intelligence',
                'field_of_study': 'Computer Science',
                'start_date': date(2024, 4, 1),
                'end_date': date(2027, 4, 30),
                'is_current': True,
                'description': 'Specializing in Artificial Intelligence and Machine Learning',
                'activities': 'IT Club of Softwarica, AI Lead',
            },
            {
                'institution': 'Liverpool Secondary School',
                'degree': '+2 NEB Computer Science',
                'field_of_study': 'Computer Science',
                'start_date': date(2021, 1, 1),
                'end_date': date(2023, 12, 31),
                'is_current': False,
            }
        ]
        
        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                institution=edu_data['institution'],
                degree=edu_data['degree'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(f'Created education: {education.degree} at {education.institution}')

        # Create Experience (including volunteering)
        experience_data = [
            {
                'title': 'AI Lead',
                'organization': 'IT Club of Softwarica',
                'experience_type': 'volunteer',
                'start_date': date(2025, 2, 1),
                'is_current': True,
                'description': 'Leading AI initiatives and organizing workshops for students. Promoting AI literacy and practical applications in technology.',
            }
        ]
        
        for exp_data in experience_data:
            experience, created = Experience.objects.get_or_create(
                title=exp_data['title'],
                organization=exp_data['organization'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'Created experience: {experience.title} at {experience.organization}')

        # Create Certifications
        certifications_data = [
            {
                'name': 'RAG Course for Beginners',
                'issuer': 'Simplilearn',
                'issue_date': date(2025, 8, 1),
                'credential_id': '8814320',
                'credential_url': 'https://simplilearn.com/certificates/8814320',
            },
            {
                'name': 'OpenCV Bootcamp',
                'issuer': 'OpenCV University',
                'issue_date': date(2025, 6, 1),
                'credential_id': 'abf20c68d09843cebe6fa3fe3c8785ee',
                'credential_url': 'https://opencv.org/certificates/abf20c68d09843cebe6fa3fe3c8785ee',
            },
            {
                'name': 'Intermediate Python',
                'issuer': 'DataCamp',
                'issue_date': date(2025, 3, 1),
                'credential_id': '76f81b24306d507e68aef7d1f08f45d824314cd2',
                'credential_url': 'https://datacamp.com/certificates/76f81b24306d507e68aef7d1f08f45d824314cd2',
            },
            {
                'name': 'Introduction to Deep Learning with PyTorch',
                'issuer': 'DataCamp',
                'issue_date': date(2025, 3, 1),
                'credential_id': 'a57dca8b3b042721d21019462246e033e3fcdf31',
                'credential_url': 'https://datacamp.com/certificates/a57dca8b3b042721d21019462246e033e3fcdf31',
            },
            {
                'name': 'Introduction to GitHub Concepts',
                'issuer': 'DataCamp',
                'issue_date': date(2025, 3, 1),
                'credential_id': '5bffef9b37f678f7ad245e0b006d2d5ae567af13',
                'credential_url': 'https://datacamp.com/certificates/5bffef9b37f678f7ad245e0b006d2d5ae567af13',
            },
        ]
        
        for cert_data in certifications_data:
            certification, created = Certification.objects.get_or_create(
                name=cert_data['name'],
                issuer=cert_data['issuer'],
                defaults=cert_data
            )
            if created:
                self.stdout.write(f'Created certification: {certification.name}')

        # Create Site Settings
        site_settings, created = SiteSettings.objects.get_or_create(
            defaults={
                'site_title': 'Biplove Gautam - Portfolio',
                'site_description': 'Portfolio of Biplove Gautam - Computer Science Student & AI Enthusiast',
                'footer_text': '© 2024 Biplove Gautam. All rights reserved.',
            }
        )
        if created:
            self.stdout.write('Created site settings')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated initial data!')
        )
