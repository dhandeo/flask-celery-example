
A simple example for Celery within Flask
----------------------------------------

Examples demonstrated
=====================

- Storing and monitoring progress of the tasks using custom states
- Polling for progress to obtain percentage progress
- Uses mongodb backend (assumed to be running at 127.0.0.1:27017

Requirements
============

The versions of my python modules are as follows

- celery==3.0.15
- celery-with-mongodb==3.0
- Flask==0.9
- pymongo==2.4.2

Getting Started
===============

In your project directory start celery:

.. code-block:: none

    python tasks.py worker --loglevel=debug

then (Probably in second command window) start the application as -

.. code-block:: none

    python app.py

Outside testing
===============

Outside testing is now obsolete, but I plan to fix it in future commits

.. code-block:: none

    python outside_test.py 

    
    