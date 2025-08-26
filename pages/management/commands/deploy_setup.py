from django.core.management.base import BaseCommand
from django.core.management import execute_from_command_line
import sys


class Command(BaseCommand):
    help = 'Setup database and static files for deployment'

    def handle(self, *args, **options):
        """
        This command is safe to run during deployment and will:
        - Run migrations
        - Create a superuser if needed (in development)
        - Collect static files
        """
        try:
            # Run migrations
            self.stdout.write('Running migrations...')
            execute_from_command_line(['manage.py', 'migrate', '--noinput'])
            self.stdout.write(self.style.SUCCESS('Migrations completed!'))
            
            # Collect static files
            self.stdout.write('Collecting static files...')
            execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--clear'])
            self.stdout.write(self.style.SUCCESS('Static files collected!'))
            
            self.stdout.write(self.style.SUCCESS('Deployment setup completed successfully!'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during setup: {str(e)}'))
            sys.exit(1)
