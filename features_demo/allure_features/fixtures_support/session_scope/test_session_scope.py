import allure
import pytest


@allure.step
def step_inside_test_body():
    pass

@allure.step
def function_scope_step():
    pass


@allure.step
def module_scope_step():
    pass


@allure.step
def class_scope_step():
    pass


@allure.step
def session_scope_step():
    pass


@pytest.fixture
def function_scope_fixture():
    function_scope_step()


@pytest.fixture(params=[True, False], ids=['param_true', 'param_false'])
def function_scope_fixture_with_finalizer(request):
    if request.param:
        print('True')
    else:
        print('False')
    def function_scope_finalizer():
        function_scope_step()
    request.addfinalizer(function_scope_finalizer)


@pytest.fixture(scope='class')
def class_scope_fixture():
    module_scope_step()


@pytest.fixture(scope='class')
def class_scope_fixture_with_finalizer(request):
    def class_finalizer_fixture():
        class_scope_step()
    request.addfinalizer(class_finalizer_fixture)


@pytest.fixture(scope='module')
def module_scope_fixture():
    module_scope_step()


@pytest.fixture(scope='module')
def module_scope_fixture_with_finalizer(request):
    def module_finalizer_fixture():
        module_scope_step()
    request.addfinalizer(module_finalizer_fixture)


@pytest.fixture(scope='session')
def session_scope_fixture():
    module_scope_step()


@pytest.fixture(scope='session')
def session_scope_fixture_with_finalizer(request):
    def session_finalizer_fixture():
        session_scope_step()
    request.addfinalizer(session_finalizer_fixture)


@allure.feature('Fixtures')
class TestClass(object):

    def test_with_scoped_fixtures(self,
                                  session_scope_fixture,
                                  function_scope_fixture,
                                  class_scope_fixture,
                                  module_scope_fixture):
        step_inside_test_body()

    def test_with_scoped_finalizers(self,
                                    function_scope_fixture_with_finalizer,
                                    class_scope_fixture_with_finalizer,
                                    module_scope_fixture_with_finalizer,
                                    session_scope_fixture_with_finalizer):
        step_inside_test_body()

