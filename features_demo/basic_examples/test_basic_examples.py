"""
This module contains basic examples of tests
"""
import pytest


def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False


@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True


@pytest.mark.xfail(condition=lambda: False, reason='this test is not expecting failure')
def test_xfail_expected_pass():
    """this test is not expected to fail, and it passed"""
    assert True


@pytest.mark.xfail(condition=lambda: False, reason='this test is not expecting failure')
def test_xfail_unexpected_failure():
    """this test is not expected to fail, but it failed"""
    assert False


def test_broken_fixture(NOT_A_FIXTURE):
    """this test fails due to a non-satisfiable fixture request"""
    assert True


def a_func(x):
    return b_func(x)


def b_func(x):
    raise RuntimeError(x)


def test_long_stacktrace():
    a_func('I am a failure reason')


def test_pytest_expansion():
    a = {1: 2, 3: 4}
    b = {1: 3, 3: 4}

    assert a == b


def test_failed_by_pytest_fail():
    pytest.fail("This test is failed by result of the pytest.fail() call")


def test_skipped_by_pytest_skip():
    pytest.skip("This test is skipped by result of the pytest.skip() call")


@pytest.mark.skipif('2 + 2 != 5', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
def test_skip_by_triggered_condition():
    pass
