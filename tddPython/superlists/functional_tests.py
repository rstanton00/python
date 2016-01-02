from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    #As a user, I want to be able to go to the expected URL to access
    #the online to-do application
    self.browser.get('http://localhost:8000')

    #User should note the appropriate title and header in the web-page
    self.assertIn('To-Do lists', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    #User should be invited to create a to-do item immediately

    #User enters a to-do item into a text box

    #User confirms entry, the page updates, and page lists the user entry

    #User can add another item to the list if desired

    #If user adds another item, page updates again and shows two items in list

    #User's list should be saved and available via a URI

    #User closes the application upon seeing the list is saved/available

if __name__ == '__main__':
  unittest.main(warnings='ignore')
