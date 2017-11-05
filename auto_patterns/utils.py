from inspect import getmembers, isfunction, getmodule, getfullargspec
from django.conf.urls import url, include

# A simple mapping between view parameter type and url regex
TYPES_REGEX = {
    "<class 'int'>": "[0-9]",
    "<class 'str'>": "[-a-zA-Z0-9/]",
}

def patterns(mod, base='', custom=None):
    """Generates a list of patterns from a views module, wrapped in a
    `django.core.urlresolvers.RegexURLResolver`.

    Views should include type hints on parameters:

        def page(request, slug: str):
            return HttpResponse()

    Examples
    --------

    >>> auto_patterns(my_views)
    url('', include([url(r'page/(?P<slug>[-a-zA-Z0-9/]+)/$', page, name='page')]))

    >>> auto_patterns(my_views, custom={'page': r'^$'})
    url('', include([url(r'^$', page, name='page')]))

    >>> auto_patterns(my_views, base='api')
    url('api', include([url(r'page/(?P<slug>[-a-zA-Z0-9/]+)/$', page, name='page')]))

    """
    if not custom:
        custom = {}

    views = getmembers(mod, isfunction)
    views = [t for t in views if getmodule(t[1]) == mod]

    urls = []

    for name, view in views:

        if name in custom:
            u = custom[name]
        else:
            annotations = getfullargspec(view).annotations

            u = r''
            u += name + "/"
            for param_name, param_type in annotations.items():
                if param_name != 'request':
                    u += "(?P<%s>%s+)/" % (param_name, TYPES_REGEX[str(param_type)])
            u += "$"

        urls.append(url(u, view, name=name))

    return url(base, include(urls))
