from django.core.management.base import BaseCommand
from pages.models import Project, ProjectImage, Skill
from datetime import date


class Command(BaseCommand):
    help = 'Create sample projects with images to demonstrate functionality'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample projects...')
        
        # Get or create some skills
        python_skill, _ = Skill.objects.get_or_create(
            name='Python',
            defaults={'category': 'Programming Languages', 'proficiency': 'advanced'}
        )
        django_skill, _ = Skill.objects.get_or_create(
            name='Django',
            defaults={'category': 'Frameworks', 'proficiency': 'intermediate'}
        )
        react_skill, _ = Skill.objects.get_or_create(
            name='React',
            defaults={'category': 'Frameworks', 'proficiency': 'intermediate'}
        )
        
        # Create a sample project
        project, created = Project.objects.get_or_create(
            title='Portfolio Website',
            defaults={
                'description': '''This is a comprehensive portfolio website built with Django and modern web technologies. 
                
Features include:
• Dynamic content management through Django admin
• Responsive design for all devices
• Image gallery with carousel functionality
• Blog integration with Medium RSS feed
• Contact form with database storage
• Cloudinary integration for image storage

The website showcases a clean, modern design with smooth animations and excellent user experience. The backend is powered by Django with PostgreSQL database, while the frontend uses vanilla JavaScript for interactions.

This project demonstrates full-stack development skills including:
- Backend development with Django
- Database design and management
- API integration (Medium RSS)
- Cloud services integration (Cloudinary, Neon DB)
- Responsive web design
- Modern CSS and JavaScript techniques''',
                'short_description': 'A modern, responsive portfolio website built with Django featuring dynamic content management and sleek design.',
                'github_url': 'https://github.com/biplovgautam/biportfolio',
                'demo_url': 'https://youtu.be/demo-video-url',
                'is_featured': True,
                'date_created': date(2025, 8, 25),
                'order': 1
            }
        )
        
        if created:
            # Add technologies to the project
            project.technologies.add(python_skill, django_skill, react_skill)
            self.stdout.write(f'Created project: {project.title}')
        
        # Create another sample project
        ai_project, created = Project.objects.get_or_create(
            title='AI Chat Application',
            defaults={
                'description': '''An intelligent chat application powered by advanced AI models with real-time conversation capabilities.

Key Features:
• Natural language processing for human-like conversations
• Real-time messaging with WebSocket connections
• Multiple AI model support (GPT, Claude, etc.)
• Conversation history and context management
• User authentication and personalization
• Mobile-responsive interface

Technical Implementation:
- FastAPI backend for high-performance API
- WebSocket connections for real-time communication
- Redis for session management and caching
- PostgreSQL for data persistence
- React frontend with modern UI components
- Docker containerization for deployment

This project showcases expertise in:
- AI/ML integration and implementation
- Real-time web applications
- Modern API development
- Database optimization
- User experience design''',
                'short_description': 'An intelligent chat application with AI-powered conversations and real-time messaging capabilities.',
                'github_url': 'https://github.com/biplovgautam/ai-chat-app',
                'demo_url': 'https://drive.google.com/file/d/demo-video',
                'is_featured': True,
                'date_created': date(2025, 7, 15),
                'order': 2
            }
        )
        
        if created:
            # Add technologies
            ai_skill, _ = Skill.objects.get_or_create(
                name='Artificial Intelligence',
                defaults={'category': 'AI/ML', 'proficiency': 'intermediate'}
            )
            fastapi_skill, _ = Skill.objects.get_or_create(
                name='FastAPI',
                defaults={'category': 'Frameworks', 'proficiency': 'intermediate'}
            )
            ai_project.technologies.add(python_skill, react_skill, ai_skill, fastapi_skill)
            self.stdout.write(f'Created project: {ai_project.title}')
        
        # Create third sample project
        ml_project, created = Project.objects.get_or_create(
            title='Machine Learning Dashboard',
            defaults={
                'description': '''A comprehensive machine learning dashboard for data analysis and model visualization.

Features:
• Interactive data visualization with charts and graphs
• Model training and evaluation tools
• Real-time performance monitoring
• Data preprocessing and cleaning utilities
• Export capabilities for reports and models
• Multi-user collaboration features

Built with modern ML stack:
- Python for data processing and ML algorithms
- Streamlit for interactive web interface
- Pandas and NumPy for data manipulation
- Scikit-learn for machine learning models
- Plotly for interactive visualizations
- MLflow for experiment tracking

This project demonstrates:
- Data science and machine learning expertise
- Interactive web application development
- Data visualization and storytelling
- ML model lifecycle management
- Performance optimization techniques''',
                'short_description': 'Interactive machine learning dashboard with data visualization and model training capabilities.',
                'github_url': 'https://github.com/biplovgautam/ml-dashboard',
                'demo_url': 'https://ml-dashboard-demo.streamlit.app/',
                'is_featured': True,
                'date_created': date(2025, 6, 10),
                'order': 3
            }
        )
        
        if created:
            # Add technologies
            ml_skill, _ = Skill.objects.get_or_create(
                name='Machine Learning',
                defaults={'category': 'AI/ML', 'proficiency': 'intermediate'}
            )
            streamlit_skill, _ = Skill.objects.get_or_create(
                name='Streamlit',
                defaults={'category': 'Frameworks', 'proficiency': 'intermediate'}
            )
            ml_project.technologies.add(python_skill, ml_skill, streamlit_skill)
            self.stdout.write(f'Created project: {ml_project.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample projects!')
        )
        self.stdout.write('You can now:')
        self.stdout.write('1. Go to http://127.0.0.1:8000/admin/ to add images to projects')
        self.stdout.write('2. Visit http://127.0.0.1:8000/ to see featured projects')
        self.stdout.write('3. Visit http://127.0.0.1:8000/projects/ to see all projects')
        self.stdout.write('4. Click on any project to see the detailed view with image slider')
