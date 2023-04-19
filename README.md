# graphene-django library
This is a follow along project from DjangoCon 21 with Dane Hillard.

<p>I have been exploring GraphQL as the most viable framework for a complex relational memory structure. This type of memory structure would have (k) applications in real world data management and graphQL's easy endpoint is super enticing. This is a minimal example of a graph implementation.
</p>
<p>
I did modify the project as shared by Dane using some of my own best-practices. I used `python-dotenv` for storing secrets and also added an authentication layer in the query using the `info.context.user.is_authenticated` from `info` given to the query.
</p>

## Project Setup

### Requirements.txt 

<p>
I recycled the `venv` for this workbook so there are a few dependencies listed that are not necessary. I did not use relay or six or sqlparse or the like for this workbook.
</p>

1. aniso8601==9.0.1
1. asgiref==3.6.0
1. Django==4.2
1. graphene==3.2.2
1. graphene-django==3.0.0
1. graphql-core==3.2.3
1. graphql-relay==3.2.0
1. promise==2.3
1. psycopg2-binary==2.9.6
1. python-dotenv==1.0.0
1. six==1.16.0
1. sqlparse==0.4.4
1. text-unidecode==1.3
1. tzdata==2023.3

### `settings.py` imports
```py
  from pathlib import Path
  from dotenv import load_dotenv
  import os
  load_dotenv()
```

### `settings.py` backend db setup:
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
<p>
I use Postgres for most projects.
</p>

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

### Graphene Schema reference in `settings.py`:
```py
  GRAPHENE = {
    "SCHEMA": "schema.schema",
  }
```
