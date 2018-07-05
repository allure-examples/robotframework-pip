# -*- coding: utf-8 -*-
import pytest
import allure


@allure.feature('Title')
@allure.title("This test has a custom title")
def test_with_a_title():
    assert 2 + 2 == 4


@allure.feature('Title')
@allure.title("This test has a custom title with unicode: Привет!")
def test_with_unicode_title():
    assert 3 + 3 == 6


@allure.feature('Title')
@allure.title("Parameterized test title: adding {param1} with {param2}")
@pytest.mark.parametrize('param1,param2,expected', [
    (2, 2, 4),
    (1, 2, 5)
])
def test_with_parameterized_title(param1, param2, expected):
    assert param1 + param2 == expected


@allure.feature('Title')
@allure.title("This title will be replaced in a test body")
def test_with_dynamic_title():
    assert 2 + 2 == 4
    allure.dynamic.title('After a successful test finish, the title was replaced with this line.')
