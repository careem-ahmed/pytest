# test_app.py
import unittest
import datetime as dt
# import mock
from helper import update_pdata

class TestApp(unittest.TestCase):

    def test_update_pdata(self):   
        existing_deposit = 10000
        increament = 100
        self.assertEqual(update_pdata(existing_deposit,increament),10100)

if __name__ == '__main__':
    unittest.main()