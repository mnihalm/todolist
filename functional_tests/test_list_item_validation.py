from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # accidentally submits empyt list item by hitting enter

        # The Homepage refreshes, and there is an error message saying list items cant be blank

        # She ties again wiht some text aand works

        # she submist another blank item

        # receives imilar warning on hte list page

        #And she can correct it by filling some text in

        self.fail('write me')
