This is an automation test using Selenium, Python and Behave(Cucumber). It provides the following automated tests for the features Login and Cart of Amazon Website.

I used Linux Mint environment to develop this automation.

Login Feature:
- Validate Successful Login on Amazon Website
- Validate message for entry with invalid email for login
		- email  not  registered
		- empty email
		- invalid email format
- Validate message for entry with an invalid password for login
		- invalid password
		- empty password field
		
Cart: 

- Search for a product and verify the list response
- Add the product to cart and verify product is added to the cart successfully
		- validate the price, quantity, and options for the product in the cart
- Validate the removal of a product in my cart


Note: Amazon sometimes requires captcha and I didn't find a way to bypass it (neither should I have), so when the website requires to fill in the captcha you need to do it manually.
First access for amazon requires e-mail validation, so I implemented a helper who does it automatically for the user. (but again, if captcha is needed you need to do it manually)

**Prerequisites**
- Python 3.6 or above
- Pip
- Behave 
- Selenium 


**Installation Guide**

If you use linux you can just type those commands and go to Step 3:

- `sudo apt install python3 python3-pip python3-behave`
- `pip3 install -r requirements.txt`

If you not, you have the follow the downloads the steps:

**_Step 1:_** Download and Install the latest version of Python on the official site: https://www.python.org/downloads/

You can find Installation Guide to your system here: https://realpython.com/installing-python/

**_Step 2:_** Install or Update pip

You can find Installation Guide to your system here: https://pypi.org/project/pip/

**_Step 3:_** Install behave and all dependencies listed on requirements.txt inside your project
Execute the command line:

- `pip install -r requirements.txt` or
- `pip3 install -r requirements.txt`

**_Step 4:_** Install Selenium and the appropriate webdrivers

You can find an installation Guide here: https://selenium-python.readthedocs.io/installation.html

**_Step 5:_** To run the test cases you can run:

 `behave`
`behave -n 'the scenario you want to run'`
`behave ./features/test_you_want.feature`