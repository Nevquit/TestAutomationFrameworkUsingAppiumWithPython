"""Environment Configuration Class"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from utils.get_args_from_cli import get_args


class Config:
	"""
	Environment Configuration Class
	Source: https://www.udemy.com/elegant-automation-frameworks-with-python-and-pytest
	"""
	def __init__(self):

		params = get_args()

		self._base_url = {
			'integration': 'http://192.168.2.3:8080',
			'production': 'https://parabank.parasoft.com',
			'localhost': 'http://localhost:8080',
		}[params['env'].lower()]

		'''
		self._is_headless = params['is_headless']

		self._browser = {
			'chrome': 'chrome',
			'edge': 'edge',
			'firefox': 'mozilla'
		}[params['browserName'].lower()]
		'''

	@property
	def base_url(self):
		return self._base_url

	'''
	@property
	def browser(self):
		return self._browser

	@property
	def is_headless(self):
		return self._is_headless

	def _print_run_config(self):
		"""
		Prints run configurations
		:return:
		"""
		print('\nRun configurations -> Browser: {}\n'
		      'Run configurations -> Environment: {}\n'
		      'Run configurations -> Is Headless: {}'.format(self.browser, self.base_url, self.is_headless))
	'''

