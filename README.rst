Allure Python demo
=====================

This repository contains extensive examples of Allure features that are available via
Allure plugin for Pytest testing framework.

- `Allure Pytest plugin <https://github.com/allure-framework/allure-python/tree/master/allure-pytest>`_

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
