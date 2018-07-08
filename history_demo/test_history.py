import allure
import random
import time


@allure.step
def passing_step():
    pass


@allure.step
def flaky_step():
    assert 1 == random.randint(1, 2)


@allure.step
def failing_step():
    assert 2 == 1


@allure.step
def broken_step():
    raise Exception('Broken!')


def test_always_passing():
    passing_step()


def test_always_failing():
    failing_step()


def test_flaky_with_randomized_time():
    passing_step()
    time.sleep(random.randint(1, 5))
    flaky_step()


def test_broken_with_randomized_time():
    passing_step()
    time.sleep(random.randint(1, 3))
    broken_step()


def test_broken():
    broken_step()


def test_with_long_execution_time():
    time.sleep(5)
