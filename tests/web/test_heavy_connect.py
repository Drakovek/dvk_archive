import unittest
from dvk_archive.web.heavy_connect import HeavyConnect


class TestHeavyConnect(unittest.TestCase):
    """
    Unit tests for the heavy_connect.py module.
    """

    def test_get_page(self):
        """
        Tests the get_page function.
        """
        connect = HeavyConnect()
        try:
            assert connect.get_page() is None
            assert connect.get_page(None) is None
            assert connect.get_page("") is None
            assert connect.get_page("jkslkeerkn") is None
            assert connect.get_page("http://lakjwj;wklk;okjovz") is None
            url = "http://pythonscraping.com/exercises/exercise1.html"
            bs = connect.get_page(url)
            if bs is None:
                assert False
            else:
                assert bs.find("h1").get_text() == "An Interesting Title"
            url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
            bs = connect.get_page(url, element="//button[@id='loadedButton']")
            if bs is None:
                assert False
            else:
                button = bs.find("button", {"id": "loadedButton"})
                assert button is not None
                assert button.get_text() == "A button to click!"
            bs = connect.get_page(url, element="//button[@id='nothing']")
            assert bs is None
        finally:
            connect.close_driver()