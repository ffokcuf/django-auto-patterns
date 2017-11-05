import re

from django.test import TestCase

from .utils import patterns
from .test_views import views as views

class PatternsTestCase(TestCase):

    def test_simple(self):
        the_patterns = patterns(views).url_patterns

        data = [
            {
                'view': views.comment,
                'regex': re.compile('comment/(?P<page_slug>[-a-zA-Z0-9/]+)/(?P<comment_id>[0-9]+)/$'),
                'name': "comment",
            },
            {
                'view': views.page,
                'regex': re.compile('page/(?P<slug>[-a-zA-Z0-9/]+)/$'),
                'name': "page",
            },
        ]

        for index, d in enumerate(data):
            self.assertEqual(the_patterns[index].callback, d['view'])
            self.assertEqual(the_patterns[index].regex, d['regex'])
            self.assertEqual(the_patterns[index].name, d['name'])

    def test_with_base(self):
        the_patterns = patterns(views, custom={'comment': r'^hello\.html$'}).url_patterns

        data = [
            {
                'view': views.comment,
                'regex': re.compile('^hello\.html$'),
                'name': "comment",
            },
            {
                'view': views.page,
                'regex': re.compile('page/(?P<slug>[-a-zA-Z0-9/]+)/$'),
                'name': "page",
            },
        ]

        for index, d in enumerate(data):
            self.assertEqual(the_patterns[index].callback, d['view'])
            self.assertEqual(the_patterns[index].regex, d['regex'])
            self.assertEqual(the_patterns[index].name, d['name'])

