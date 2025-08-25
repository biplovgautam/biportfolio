import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from django.conf import settings
from .models import Blog
import re


def fetch_medium_blogs():
    """
    Fetch blogs from Medium RSS feed and save them to database
    """
    try:
        medium_username = settings.MEDIUM_USERNAME
        if not medium_username or medium_username == '@yourusername':
            return False, "Medium username not configured"
        
        # Medium RSS feed URL
        rss_url = f"https://medium.com/feed/{medium_username}"
        
        response = requests.get(rss_url, timeout=10)
        response.raise_for_status()
        
        # Parse RSS feed
        root = ET.fromstring(response.content)
        
        # Find all items (blog posts)
        items = root.findall('.//item')
        
        new_blogs_count = 0
        
        for item in items:
            try:
                title = item.find('title').text
                link = item.find('link').text
                description = item.find('description').text
                pub_date = item.find('pubDate').text
                
                # Parse publication date
                pub_date_obj = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %Z')
                
                # Extract Medium post ID from link
                medium_post_id = link.split('/')[-1] if '/' in link else ''
                
                # Clean description (remove HTML tags)
                clean_description = re.sub('<.*?>', '', description) if description else ''
                clean_description = clean_description[:500] + '...' if len(clean_description) > 500 else clean_description
                
                # Extract tags if available
                tags = []
                categories = item.findall('category')
                for cat in categories:
                    if cat.text:
                        tags.append(cat.text)
                tags_str = ', '.join(tags)
                
                # Check if blog already exists
                if not Blog.objects.filter(medium_post_id=medium_post_id).exists():
                    Blog.objects.create(
                        title=title,
                        description=clean_description,
                        url=link,
                        published_date=pub_date_obj,
                        tags=tags_str,
                        medium_post_id=medium_post_id,
                        is_featured=False
                    )
                    new_blogs_count += 1
                    
            except Exception as e:
                print(f"Error processing blog item: {str(e)}")
                continue
        
        return True, f"Successfully fetched {new_blogs_count} new blogs"
        
    except requests.RequestException as e:
        return False, f"Error fetching Medium RSS: {str(e)}"
    except ET.ParseError as e:
        return False, f"Error parsing RSS feed: {str(e)}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"


def auto_sync_medium_blogs():
    """
    Automatically sync Medium blogs - can be called from views or management commands
    """
    return fetch_medium_blogs()
