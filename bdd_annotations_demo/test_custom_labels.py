import allure
import pytest


@allure.step
def simple_step():
    pass


@allure.feature('Label')
@allure.label('tag2', 'value')
def test_with_custom_label_and_feature():
    simple_step()


@allure.feature('Label')
@allure.label('tag1', 'value1', 'value2')
def test_with_a_custom_label_and_multiple_values():
    simple_step()


@allure.feature('Label')
@allure.label('tag1', 'initial_value')
def test_dynamic_label():
    simple_step()
    allure.dynamic.label('tag1', 'added_value')


@allure.feature('Label')
@pytest.mark.special
def test_pytest_marker():
    simple_step()


@allure.feature('Label')
@pytest.mark.marker('marker_value')
def test_pytest_marker_tag_with_value():
    simple_step()
