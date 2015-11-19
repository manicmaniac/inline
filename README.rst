inline
======

.. image:: https://img.shields.io/travis/manicmaniac/inline/master.svg
    :target: https://travis-ci.org/manicmaniac/inline
    :alt: Travis CI

.. image:: https://img.shields.io/pypi/v/inline.svg
    :target: https://pypi.python.org/pypi/inline
    :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/inline.svg
    :target: https://pypi.python.org/pypi/inline
    :alt: Python Versions

Embed inline C / C++ source codes in Python.

Usage
-----

.. code:: python

    import inline
    c = inline.c(r'''
    int add(int a, int b) {
        return a + b;
    }
    ''')
    c.add(40, 2)


.. code:: python

    import inline
    cxx = inline.cxx(r'''
    extern "C" {
        int add(int a, int b) {
            return a + b;
        }
    }
    ''')
    cxx.add(40, 2)


Install
-------

.. code:: sh

    pip install inline

.. code:: sh

    git clone https://github.com/manicmaniac/inline.git
    cd inline
    python setup.py install
