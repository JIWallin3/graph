# graphene-django library
This is a follow along project from DjangoCon 21 with Dane Hillard.

I have been exploring GraphQL as the most viable framework for a complex relational memory structure. This type of memory structure would have (k) applications in real world data management and graphQL's easy endpoint is super enticing. This is a minimal example of a graph implementation.

## Project Setup

### Requirements
1. python==v3.9
2. Django==4.2
3. graphene-django==3.0.0
4. psycopg2-binary==2.9.6
5. python-dotenv==1.0.0

### Settings.py imports
```py
  from pathlib import Path
  from dotenv import load_dotenv
  import os
  load_dotenv()
```

### Database Backend
```py
  DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.environ.get('DB_NAME'),
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASSWORD'),
    'HOST': os.environ.get('DB_HOST'),
    'PORT': '',
    }
  }
```

### Static Files
```py
  STATIC_URL = "/static/"
  # Set the STATIC_ROOT setting to a valid filesystem path where Django can collect static files
  STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

  STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
  ]
```
