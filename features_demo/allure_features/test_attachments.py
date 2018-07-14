"""Test that demonstrate some of the examples how attachments can be used."""

import pytest
import allure


@pytest.fixture(scope='module')
def attachment_in_module_scope_fixture():
    allure.attach('A text attacment in module scope fixture', 'blah blah blah', allure.attachment_type.TEXT)


@pytest.fixture
def attach_file_in_function_scope_fixture():
    allure.attach.file('./data/rick.mp4', attachment_type=allure.attachment_type.MP4)


@allure.step
def step1():
    allure.attach.file('./data/cat.mp4', attachment_type=allure.attachment_type.MP4)


@allure.feature('Attachments')
def test_with_attachment_in_fixture(attach_file_in_function_scope_fixture):
    pass


@allure.feature('Attachments')
def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_finalizer):
    pass


@allure.feature('Attachments')
def test_multiple_attachments():
    allure.attach.file('./data/totally_open_source_kitten.png', attachment_type=allure.attachment_type.PNG)
    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)


@allure.feature('Attachments')
def test_attachment_in_step():
    step1()


@pytest.fixture
def attach_file_in_function_scope_finalizer(request):
    def finalizer_function_scope_fixture():
        allure.attach('A text attacment in function scope finalizer', 'blah blah', allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_function_scope_fixture)


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('A text attacment in module scope fixture', 'blah blah blah', allure.attachment_type.TEXT)
    def finalizer_module_scope_fixture():
        allure.attach('A text attacment in module scope finalizer', 'blah blah blah blah',
                      allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_module_scope_fixture)
