import unittest
from similarweb import utils
from similarweb.exceptions import InvalidURLException


class TestUtils(unittest.TestCase):

    def test_domain_from_url(self):
        # should raise exceptions for invalid url
        self.assertRaises(InvalidURLException, utils.domain_from_url, "INVALID")

        # should return root domain
        self.assertEqual(utils.domain_from_url("google.com"), "google.com")
        self.assertEqual(utils.domain_from_url("http://google.com/sg/?q=search"), "google.com")
        self.assertEqual(utils.domain_from_url("http://sg.google.com/page/?q=search"), "google.com")
