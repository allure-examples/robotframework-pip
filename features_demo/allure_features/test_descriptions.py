# -*- coding: utf-8 -*-
import allure


@allure.feature('Description')
def test_with_print():
    """this one prints something to stdout"""

    print('Hello')


@allure.feature('Description')
def test_with_stderr():
    """this one prints something to stdderr"""

    import sys

    sys.stderr.write('hello\n\n\nthere')


@allure.feature('Description')
def test_with_stderr_and_stdout():
    """this one prints something to both stdderr and stdout"""

    import sys

    sys.stdout.write('this goes to stdout\n\n')
    sys.stderr.write('this goes to stderr')


@allure.feature('Description')
@allure.description_html("""
<h1>Test with some complicated html description</h1>
<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr align="center">
    <td>William</td>
    <td>Smith</td> 
    <td>50</td>
  </tr>
  <tr align="center">
    <td>Vasya</td>
    <td>Jackson</td> 
    <td>94</td>
  </tr>
</table>
""")
def test_html_description():
    assert True


@allure.feature('Description')
@allure.description("""
Multiline test description.
That comes from the allure.description annotation.

Nothing special about it.
""")
def test_description_from_annotation():
    assert 42 == int(6 * 7)


@allure.feature('Description')
def test_unicode_in_docstring_description():
    """Unicode in description.

    Этот тест проверяет юникод.

    你好伙计.
    """
    assert 42 == int(6 * 7)


@allure.feature('Description')
@allure.description("""
This description will be replaced at the end of the test.
""")
def test_dynamic_description():
    assert 42 == int(6 * 7)
    allure.dynamic.description('A final description.')