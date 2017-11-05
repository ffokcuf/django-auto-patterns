# django-auto-patterns

django-auto-patterns automatically creates Django [RegexURLResolver](https://docs.djangoproject.com/fr/1.11/_modules/django/urls/resolvers/) using views name/parameter types.

Uses type [hints under](https://docs.python.org/3/library/typing.html) the hood to map views parameters to url pattern parts.

## Installation

In `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'auto_patterns',
]
```

## Basic usage

In `urls.py`:

```python
from auto_patterns import patterns

import myapp.views as views

urlpatterns = [
    patterns(views, base='api', custom={'home': r'^$'}),
]
```

In the previous example, all functions in *myapp/views.py* will be routed on **api/`function name`/`param 1`/`param 2`/…**, except `home` which be routed on **api/**.

## Limitations

- Only works with [function based views](https://docs.djangoproject.com/en/1.11/topics/http/views/).

## Tests

```shell
python manage.py test auto_patterns
```

