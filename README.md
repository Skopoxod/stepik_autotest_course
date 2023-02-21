# stepik_autotest_course

This is a test repo for Stepik course https://stepik.org/course/575

You need to install Selenium framework and a Chrome or Firefox driver to use autotest scrits.
More info here: https://pypi.org/project/selenium/

Scripts can be located in Scripts folder. Here are some basic autotests.

test_items.py is test for check button availability in different interfaces. 
It can be used via command: pytest -s -v --language=fr test_items.py
conftest.py is required to check this case.
