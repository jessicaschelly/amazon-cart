# Amazon Cart Automation

**Install Python/behave framework**

**IMPORTANT -->> This automation needs Python 3.6 or above**

**_Step 1:_** Download and Install the latest version of Python on the official site: https://www.python.org/downloads/

You can find Installation Guide to your system here: https://realpython.com/installing-python/

**_Step 2:_** Install or Update pip

You can find Installation Guide to your system here: https://pypi.org/project/pip/

**_Step 3:_** Install behave and all dependencies listed on requirements.txt inside your project
Execute the command line:

- `pip install -r requirements.txt`

**_Step 4:_** Install Selenium and the apropriate webdrivers

You can find a installation Guide here: https://selenium-python.readthedocs.io/installation.html

But if you use linux you can just type those commands:

- `sudo apt install python3 python3-pip python3-behave`
- `pip3 install -r requirements.txt`

To run the test cases you can use:

- `behave`
- `behave -n 'the scenario you want to run'`
- `behave ./features/test_you_want.feature`