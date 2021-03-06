"""Admin Page Locator Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from selenium.webdriver.common.by import By

from tests.web_app_tests.parabank_test.page_locators.base_page_locator import BasePageLocator


class AdminPageLocator(BasePageLocator):
	"""
	Admin Page Locator Class

	Holds all relevant locators for 'Admin' page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	"""

	INITIALIZE_BUTTON = (By.XPATH, '//button[contains(text(),\'Initialize\')]')

	CLEAN_BUTTON = (By.XPATH, '//button[contains(text(),\'Clean\')]')
