def test():
    assert 1 + 1 == 2

from selenium.webdriver.common.keys import Keys
from pylenium.driver import Pylenium

def test_ah_search(py: Pylenium):
    py.visit('https:ah.nl')
    py.get('[name="q"]').type('groente', Keys.ENTER)
    py.webdriver.find_element()
    assert py.should().contain_title('groente')