import pytest
import allure


@allure.step
def step_1():
    """Step description."""
    print("Hi, I'm a step.")


@pytest.fixture
def fixture_with_passed_finalizer_and_step(request):
    def passed_finalizer():
        step_1()
    request.addfinalizer(passed_finalizer)


@pytest.fixture
def fixture_with_passed_finalizer(request):
    def passed_finalizer():
        pass
    request.addfinalizer(passed_finalizer)


@pytest.fixture
def fixture_with_failed_finalizer(request):
    def failed_finalizer():
        assert False
    request.addfinalizer(failed_finalizer)


@pytest.fixture
def fixture_with_broken_finalizer(request):
    def broken_finalizer():
        raise Exception('Ouch!')
    request.addfinalizer(broken_finalizer)


@pytest.fixture
def fixture_with_two_finalizers(request):
    def first_finalizer():
        pass
    request.addfinalizer(first_finalizer)

    def second_finalizer():
        pass
    request.addfinalizer(second_finalizer)


@allure.feature('Fixtures')
def test_two_fixures_with_finalizer(fixture_with_passed_finalizer, fixture_with_failed_finalizer):
    pass


@allure.feature('Fixtures')
def test_fixture_with_two_finalizers(fixture_with_two_finalizers):
    pass


@allure.feature('Fixtures')
def test_fixture_with_broken_finalizer(fixture_with_broken_finalizer):
    pass


@allure.feature('Fixtures')
def test_fixture_with_broken_finalizer(fixture_with_passed_finalizer_and_step):
    pass
