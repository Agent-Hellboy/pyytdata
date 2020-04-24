from pyytdata.pyytdata import PyYtData
import os

import unittest
class TestPyYtData(unittest.TestCase):

	def test_check_env(self):
		self.assertTrue(os.environ.get('API_KEY')!=None)
		

	def test_apiall(self):
		_api=PyYtData('flask',10)
		api=str(type(_api))
		print(api)		
		self.assertTrue( api == "<class 'pyytdata.pyytdata.PyYtData'>") # I have to convert the name 
                                                                                # of the class to string it would 
                                                                                # we benificial if we have var_dump() function as in php

	def test_check_google_application_credential_env(self):
		self.assertTrue(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')!=None)

if __name__=='__main__':
	unittest.main()
