from django.test import SimpleTestCase

from ..utils import strip_spaces_in_template


class TemplateStrippingTestCase(SimpleTestCase):

    def test_html_stripping(self):
        source = """<html>
                <header><title>This is title</title></header>
                <body>
                Hello world
                </body>
                </html>"""
        result = strip_spaces_in_template(source)
        expected = """<html><header><title>This is title</title></header><body>
                Hello world
                </body></html>"""
        self.assertEqual(result, expected)

    def test_template_stripping(self):
        source = """{% if latest_question_list %}
                        <ul>
                        {% for question in latest_question_list %}
                            <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
                        {% endfor %}
                        </ul>
                    {% else %}
                        <p>No polls are available.</p>
                    {% endif %}"""
        result = strip_spaces_in_template(source)
        expected = '{% if latest_question_list %} <ul> {% for question in latest_question_list %} '\
                   '<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li> {% endfor %} '\
                   '</ul> {% else %} <p>No polls are available.</p> {% endif %}'
        self.assertEqual(result, expected)
