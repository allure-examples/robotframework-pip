import pytest
import allure


@allure.step
def step1():
    pass


@pytest.fixture
def function_scope_simple_fixture():
    pass


@pytest.fixture
def function_scope_fixture_2():
    step1()


@pytest.fixture
def nested_function_scope_fixture(function_scope_simple_fixture):
    pass


@pytest.fixture
def function_scope_fixture_with_several_deps(function_scope_simple_fixture, function_scope_fixture_2):
    pass


@pytest.fixture(params=[True, False], ids=['param_true', 'param_false'])
def parametrized_fixture_with_ids(request):
    return request.param


@allure.feature('Fixtures')
def test_parameterized_fixture(parametrized_fixture_with_ids):
    pass


@allure.feature('Fixtures')
def test_with_simple_fixture_in_function_scope(function_scope_simple_fixture):
    pass


@allure.feature('Fixtures')
def test_with_nested_fixtures_in_function_scope(nested_function_scope_fixture):
    pass


@allure.feature('Fixtures')
def test_with_function_scope_fixture_with_several_deps(function_scope_fixture_with_several_deps):
    pass
