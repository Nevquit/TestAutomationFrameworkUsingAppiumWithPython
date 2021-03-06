"""Test User Login with Wrong Credentials"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import pytest

from utils.get_args_from_cli import get_args
from selenium.common.exceptions import NoSuchElementException

from tests.config import Config
from tests.web_app_tests.parabank_test.expected_results.users.base_user import BaseUser
from tests.web_app_tests.parabank_test.helper_methods.register_user import register_user
from tests.web_app_tests.parabank_test.helper_methods.clean_database import clean_database
from tests.web_app_tests.parabank_test.page_object_models.home_page_model import HomePageModel
from tests.web_app_tests.parabank_test.expected_results.users.valid_users_templates.jane_doe import JaneDoe
from tests.web_app_tests.parabank_test.expected_results.page_content.home_page_content import HomePageContent
from tests.web_app_tests.parabank_test.expected_results.page_content.login_page_content import LoginPageContent
from tests.web_app_tests.parabank_test.base_case.android_browser_base_testcase import AndroidBrowserBaseTestCase
from tests.web_app_tests.parabank_test.page_object_models.account_services_menu_model import AccountServicesMenuModel


@allure.epic('ParaBank Web App')
@allure.parent_suite('End To End')
@allure.suite("User Login/Logout")
@allure.sub_suite("Negative Tests")
@allure.feature("Home Page")
@allure.story('Login/Logout Functionality')
@pytest.mark.skipif(get_args()['env'] == 'production',
                    reason="This is demo test that usually fails on production environment. "
                           "Therefore, it will have negative effect on Travis CI status.")
class TestUserLoginWrongCredentials(AndroidBrowserBaseTestCase):
    """
    Test User Login -> Wrong Credentials Test Case
    """

    def test_user_login_with_wrong_password(self):
        allure.dynamic.description("""
                User Log In validation > Wrong password:
                    
                    Prerequisites: DB is clean, user is registered, web browser is opened
                    
                    Step by step:
                    1. Open Home web page
                    2. Do URL verification
                    3. Do Title verification
                    4. Type correct username + wrong password
                    5. Hit "Log In" button
                    6. Verify Page Title
                    7. Verify error title
                    8. Verify error message
                    9. Do URL verification
                    10. Verify that "Account Services" menu is not displayed
                    11. Close web browser
                """)
        allure.dynamic.title("Home Page > User Log In validation > Wrong password")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        config = Config()
        user = BaseUser(JaneDoe)

        with allure.step("Initial data setup > clean DB"):
            clean_database(driver=self.driver,
                           config=config)

        with allure.step("Initial data setup > register test user"):
            register_user(driver=self.driver,
                          user=user,
                          config=config)

        with allure.step("Open web browser"):
            page = HomePageModel(config=config,
                                 driver=self.driver,
                                 explicit_wait_time=10)

        # 1. Open Home web page
        with allure.step("Open web page"):
            page.go()

        # 2. Do URL verification
        with allure.step("Verify web page URL"):
            assert config.base_url + HomePageContent.URL == page.url

        # 3. Do Title verification
        with allure.step("Verify web page title"):
            assert HomePageContent.TITLE == page.title

        # 4. Type username
        with allure.step("Type username"):
            page.customer_login.enter_username(user.username)

        # 4. Type password
        with allure.step("Type password"):
            page.customer_login.enter_password('wrongpassword')

        # 5. Hit "Log In" button
        with allure.step("Hit \"Log In\" button"):
            page = page.customer_login.hit_login_button()

        # 6. Verify page title
        with allure.step("Verify page title"):
            assert LoginPageContent.TITLE == page.title

        # 7. Verify error title
        with allure.step("Verify error title"):
            assert LoginPageContent.ERROR_TITLE == page.error_title

        # 8. Verify error message
        with allure.step("Verify error message"):
            assert LoginPageContent.NO_SUCH_USER_ERROR_MESSAGE == page.error_message

        # 9. Do URL verification
        with allure.step("Do URL verification"):
            assert config.base_url + LoginPageContent.URL == page.url

        # 10. Verify that "Account Services" menu is not displayed
        with allure.step("Verify that \"Account Services\" menu is not displayed"):
            with pytest.raises(NoSuchElementException):
                AccountServicesMenuModel(config=config,
                                         driver=self.driver,
                                         explicit_wait_time=10).menu_title()

        # 11. Close web browser
        with allure.step("Close web browser"):
            page.close()

    def test_user_login_empty_fields(self):
        allure.dynamic.description("""
                User Log In validation > Empty fields:

                    Prerequisites: DB is clean, user is registered, web browser is opened

                    Step by step:
                    1. Open Home web page
                    2. Do URL verification
                    3. Do Title verification
                    4. Enter empty string as username/password
                    5. Hit "Log In" button
                    6. Verify Page Title
                    7. Verify error title
                    8. Verify error message
                    9. Do URL verification
                    10. Verify that "Account Services" menu is not displayed
                    11. Close web browser
                """)
        allure.dynamic.title("Home Page > User Log In validation > Empty fields")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        config = Config()
        user = BaseUser(JaneDoe)

        with allure.step("Initial data setup > clean DB"):
            clean_database(driver=self.driver,
                           config=config)

        with allure.step("Initial data setup > register test user"):
            register_user(driver=self.driver,
                          user=user,
                          config=config)

        with allure.step("Open web browser"):
            page = HomePageModel(config=config,
                                 driver=self.driver,
                                 explicit_wait_time=10)

        # 1. Open Home web page
        with allure.step("Open web page"):
            page.go()

        # 2. Do URL verification
        with allure.step("Verify web page URL"):
            assert config.base_url + HomePageContent.URL == page.url

        # 3. Do Title verification
        with allure.step("Verify web page title"):
            assert HomePageContent.TITLE == page.title

        # 4. Type username
        with allure.step("Type username"):
            page.customer_login.enter_username(user.username)

        # 4. Type password
        with allure.step("Type password"):
            page.customer_login.enter_password('')

        # 5. Hit "Log In" button
        with allure.step("Hit \"Log In\" button"):
            page = page.customer_login.hit_login_button()

        # 6. Verify page title
        with allure.step("Verify page title"):
            assert LoginPageContent.TITLE == page.title

        # 7. Verify error title
        with allure.step("Verify error title"):
            assert LoginPageContent.ERROR_TITLE == page.error_title

        # 8. Verify error message
        with allure.step("Verify error message"):
            assert LoginPageContent.EMPTY_FIELDS_ERROR_MESSAGE == page.error_message

        # 9. Do URL verification
        with allure.step("Do URL verification"):
            assert config.base_url + LoginPageContent.URL == page.url

        # 10. Verify that "Account Services" menu is not displayed
        with allure.step("Verify that \"Account Services\" menu is not displayed"):
            with pytest.raises(NoSuchElementException):
                AccountServicesMenuModel(config=config,
                                         driver=self.driver,
                                         explicit_wait_time=10).menu_title()

        # 11. Close web browser
        with allure.step("Close web browser"):
            page.close()

    def test_user_login_wrong_username(self):
        allure.dynamic.description("""
                User Log In validation > Wrong username:

                    Prerequisites: DB is clean, user is registered, web browser is opened

                    Step by step:
                    1. Open Home web page
                    2. Do URL verification
                    3. Do Title verification
                    4. Enter wrong username + correct password
                    5. Hit "Log In" button
                    6. Verify Page Title
                    7. Verify error title
                    8. Verify error message
                    9. Do URL verification
                    10. Verify that "Account Services" menu is not displayed
                    11. Close web browser
                """)
        allure.dynamic.title("Home Page > User Log In validation > Wrong username")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        config = Config()
        user = BaseUser(JaneDoe)

        with allure.step("Initial data setup > clean DB"):
            clean_database(driver=self.driver,
                           config=config)

        with allure.step("Initial data setup > register test user"):
            register_user(driver=self.driver,
                          user=user,
                          config=config)

        with allure.step("Open web browser"):
            page = HomePageModel(config=config,
                                 driver=self.driver,
                                 explicit_wait_time=10)

        # 1. Open Home web page
        with allure.step("Open web page"):
            page.go()

        # 2. Do URL verification
        with allure.step("Verify web page URL"):
            assert config.base_url + HomePageContent.URL == page.url

        # 3. Do Title verification
        with allure.step("Verify web page title"):
            assert HomePageContent.TITLE == page.title

        # 4. Type username
        with allure.step("Type username"):
            page.customer_login.enter_username('nosuchuser')

        # 4. Type password
        with allure.step("Type password"):
            page.customer_login.enter_password(user.password)

        # 5. Hit "Log In" button
        with allure.step("Hit \"Log In\" button"):
            page = page.customer_login.hit_login_button()

        # 6. Verify page title
        with allure.step("Verify page title"):
            assert LoginPageContent.TITLE == page.title

        # 7. Verify error title
        with allure.step("Verify error title"):
            assert LoginPageContent.ERROR_TITLE == page.error_title

        # 8. Verify error message
        with allure.step("Verify error message"):
            assert LoginPageContent.NO_SUCH_USER_ERROR_MESSAGE == page.error_message

        # 9. Do URL verification
        with allure.step("Do URL verification"):
            assert config.base_url + LoginPageContent.URL == page.url

        # 10. Verify that "Account Services" menu is not displayed
        with allure.step("Verify that \"Account Services\" menu is not displayed"):
            with pytest.raises(NoSuchElementException):
                AccountServicesMenuModel(config=config,
                                         driver=self.driver,
                                         explicit_wait_time=10).menu_title()

        # 11. Close web browser
        with allure.step("Close web browser"):
            page.close()