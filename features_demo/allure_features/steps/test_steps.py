import allure
from .steps import imported_step


@allure.step
def passing_step():
    pass


@allure.step
def step_with_nested_steps():
    nested_step()


@allure.step
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step
def nested_step_with_arguments(arg1, arg2):
    pass


@allure.step('Step with specific title.')
def step_with_title():
    pass


@allure.feature('Steps')
def test_with_imported_step():
    passing_step()
    imported_step()


@allure.feature('Steps')
def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()


@allure.feature('Steps')
def test_with_step_in_fixture_from_conftest(fixture_with_conftest_step):
    passing_step()


@allure.feature('Steps')
def test_with_named_step():
    step_with_title()


@allure.step
def step_with_default_args(arg1, arg2=None, arg3='default'):
    pass


@allure.feature('Steps')
def test_steps_with_default_arguments():
    step_with_default_args(1)
    step_with_default_args(2, arg3='something')
    step_with_default_args(3, True, 'anything')
    step_with_default_args(4, arg2=False, arg3='everything')


@allure.step('Step with placeholders in the title, positional: "{0}", keyword: "{key}"')
def step_with_title_placeholders(arg1, key=None):
    pass


@allure.feature('Steps')
def test_steps_with_placeholders():
    step_with_title_placeholders(1, key='something')
    step_with_title_placeholders(2)
    step_with_title_placeholders(3, 'anything')


class TestClass(object):

    @allure.step
    def step_from_test_class(self, arg):
        pass

    @allure.feature('Steps')
    def test_in_test_class_with_steps_from_different_scopes(self):
        passing_step()
        self.step_from_test_class('qq!')
