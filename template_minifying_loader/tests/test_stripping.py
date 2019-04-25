from django.test import SimpleTestCase

from ..utils import strip_spaces_in_template


class strip_spaces_in_template_TestCase(SimpleTestCase):

    def test_strip_spaces_around_variables(self):
        html = """
        <div>
            {{ _('Sign in') }}
        </div>"""

        result = strip_spaces_in_template(html)
        expected = """<div>{{ _('Sign in') }}</div>"""

        self.assertEqual(result, expected)

    def test_strip_spaces_around_tags(self):
        html = """
        <div>
            {% if user.is_anonymous %}
                <div></div>
            {% endif %}
        </div>
        """

        result = strip_spaces_in_template(html)
        expected = """<div>{% if user.is_anonymous %}<div></div>{% endif %}</div>"""

        self.assertEqual(result, expected)

    def test_strip_spaces_between_tags(self):
        html = """
        {% load i18n %}

        {% if user.is_anonymous %}
            <div></div>
        {% endif %}
        """

        result = strip_spaces_in_template(html)
        expected = """{% load i18n %}{% if user.is_anonymous %}<div></div>{% endif %}"""

        self.assertEqual(result, expected)

    def test_strip_spaces_between_html_tags(self):
        html = """
        <div>
            <div></div>
        </div>
        """

        result = strip_spaces_in_template(html)
        expected = """<div><div></div></div>"""

        self.assertEqual(result, expected)

    def test_remove_django_comments(self):
        html = """
        <div>

        {# some comment #}

        </div>
        """

        result = strip_spaces_in_template(html)
        expected = """<div></div>"""

        self.assertEqual(result, expected)

    def test_strip_spaces_between_tags_and_variables(self):
        html = """
        {% if user.is_anonymous %}
            {{ 'test' }}
        {% endif %}
        """

        result = strip_spaces_in_template(html)
        expected = """{% if user.is_anonymous %}{{ 'test' }}{% endif %}"""

        self.assertEqual(result, expected)

    def test_multiple_spaces(self):
        html = """
        <a href=""
            class="">
        """
        result = strip_spaces_in_template(html)
        expected = """<a href="" class="">"""

        self.assertEqual(result, expected)
