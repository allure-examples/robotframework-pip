Allure 2 Pytest Demo
=====================

This repository contains extensive examples of Allure 2 features that are available via
Allure 2 plugin for Pytest testing framework.

- `Allure 2 Pytest plugin <https://github.com/allure-framework/allure-python/tree/master/allure-pytest>`_

Installation and Usage
======================

To install and run test examples use the following commands that will output report data into ``/tmp/allure_results``
temporary folder.

.. code:: bash

    $ python setup.py install
    $ py.test features_demo --alluredir=/tmp/allure_results

To see the generated report execute

.. code:: bash

   $ allure serve /tmp/allure_results