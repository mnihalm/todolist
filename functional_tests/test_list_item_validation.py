from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # accidentally submits empyt list item by hitting enter
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # The Homepage refreshes, and there is an error message saying list items cant be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # She tries again with some text and it works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # she submits another blank item
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # receives similar warning on the list page
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        #And she can correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
