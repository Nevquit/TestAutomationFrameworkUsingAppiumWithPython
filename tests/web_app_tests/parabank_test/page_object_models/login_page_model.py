"""Login Page Model Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from tests.config import Config
from tests.web_app_tests.parabank_test.page_object_models.customer_login_model import CustomerLoginModel
from utils.driver import Driver

from tests.web_app_tests.parabank_test.page_locators.login_page_locator import LoginPageLocator
from tests.web_app_tests.parabank_test.page_object_models.base_page_object_model import BasePageObjectModel
from tests.web_app_tests.parabank_test.expected_results.page_content.login_page_content import LoginPageContent


class LoginPageModel(BasePageObjectModel):
	"""
	Login Page Model Class
	The page object pattern intends creating an object for each web page.
	By following this technique a layer of separation between the test code and technical implementation is created.
	"""

	def __init__(self, config: Config, driver: Driver, explicit_wait_time):

		super().__init__(config=config,
		                 driver=driver,
		                 explicit_wait_time=explicit_wait_time)
		self._locator = LoginPageLocator
		self._url = config.base_url + LoginPageContent.URL
		self._customer_login = CustomerLoginModel(driver=driver,
		                                          config=config,
		                                          explicit_wait_time=explicit_wait_time)

	@property
	def customer_login(self):
		"""
		Returns Customer Login object
		:return:
		"""
		return self._customer_login

	@property
	def error_title(self):
		"""
		Returns error title text
		:return:
		"""
		locator = self._locator.ERROR_TITLE
		return self.get_text_property(locator)

	@property
	def error_message(self):
		"""
		Returns error message text
		:return:
		"""
		locator = self._locator.ERROR_MESSAGE
		return self.get_text_property(locator)


