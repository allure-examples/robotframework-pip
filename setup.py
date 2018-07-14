from setuptools import setup


VERSION = '1.0'

install_requires = [
    'pytest>=3.5.1',
    'pytest-rerunfailures>=4.1',
    'allure-pytest>=2.5.0',
    'allure-python-commons>=2.5.0'
]


def main():
    setup(
        name='allure2-pytest-demo',
        version=VERSION,
        description='Allure 2 report features demo for Pytest testing framework',
        author='ehborisov',
        packages=['bdd_annotations_demo', 'features_demo', 'history_demo'],
        url='https://github.com/allure-examples/allure2-pytest-demo',
        install_requires=install_requires
    )


if __name__ == '__main__':
    main()
