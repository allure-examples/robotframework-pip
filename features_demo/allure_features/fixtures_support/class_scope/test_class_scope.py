import pytest
import allure


@allure.step
def class_scope_step():
    pass


@allure.step
def function_scope_step():
    pass


@pytest.fixture
def function_scope_fixture():
    function_scope_step()


@pytest.fixture(scope='class')
def class_scope_fixture():
    class_scope_step()


@pytest.fixture(scope='class')
def class_scope_fixture_with_finalizer(request):
    def finalizer_fixture():
        pass
    request.addfinalizer(finalizer_fixture)


@allure.feature('Fixtures')
class TestClass(object):

    def test_with_class_scope_finalizer(self, class_scope_fixture_with_finalizer):
        pass

    def test_with_class_scope_fixture_and_finalizer(self, class_scope_fixture, class_scope_fixture_with_finalizer):
        pass

    def test_with_class_and_function_scope_fixtures(self, class_scope_fixture, function_scope_fixture):
        pass


@allure.feature('Fixtures')
def test_without_class_scope_fixtures():
    function_scope_step()
