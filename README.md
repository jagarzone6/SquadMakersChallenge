# SquadMakersChallenge
This challenge is implemented with behave + selenium in Python 3.8


## Set up instructions
You need google chrome installed locally

1. Install pyhton 3.8 or higher https://www.python.org/downloads/release/python-380/
2. Install pipenv https://pypi.org/project/pipenv/
3. Install allure from https://github.com/allure-framework/allure2/releases
4. Install dependencies:

            pipenv install

5. Execute the tests

            pipenv run behave -f html -o report/

6. generate HTML report with allure

            sudo allure serve report/

7. Open report in your browser http://127.0.1.1:38923/
