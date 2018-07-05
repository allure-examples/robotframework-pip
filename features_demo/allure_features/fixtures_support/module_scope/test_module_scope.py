import pytest
import allure


@allure.step
def function_scope_step():
    pass


@allure.step
def module_scope_step():
    pass


@pytest.fixture(scope='module', params=[1, 2])
def module_scope_parametrized_fixture():
    module_scope_step()


@pytest.fixture(scope='module')
def module_scope_fixture():
    module_scope_step()


@pytest.fixture
def function_scope_fixture():
    function_scope_step()


@pytest.fixture(scope='module')
def module_scope_fixture_with_finalizer(request):
    def finalizer_fixture():
        pass
    request.addfinalizer(finalizer_fixture)


@allure.feature('Fixtures')
def test_module_scope_fixture(module_scope_fixture):
    pass


@allure.feature('Fixtures')
def test_module_scope_fixture_and_finalizer(module_scope_fixture, module_scope_fixture_with_finalizer):
    pass


@allure.feature('Fixtures')
def test_parameterized_module_scope_fixture(module_scope_parametrized_fixture):
    pass


@allure.feature('Fixtures')
def test_module_and_function_scope_fixtures(module_scope_fixture, function_scope_fixture):
    pass
