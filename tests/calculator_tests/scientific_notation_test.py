"""Scientific Notation Conversion"""
#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
from tests.calculator_tests.calculator_base_testcase import AndroidCalculatorBaseTestCase


@allure.epic('Android Native App')
@allure.parent_suite('Functional Test')
@allure.suite("Calculator Test Suite")
@allure.sub_suite("Positive Tests")
@allure.feature("Scientific Notation")
@allure.story('Scientific Notation Conversion')
class TestScientificNotationConversionCase(AndroidCalculatorBaseTestCase):

	pass
