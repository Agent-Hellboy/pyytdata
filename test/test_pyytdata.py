from pyytdata.pyytdata import PyYtData
import os

import unittest
class TestPyYtData(unittest.TestCase):

	def test_check_env(self):
		self.assertTrue(os.environ.get('API_KEY')!=None)
	

	def test_apiall(self):
		_api=PyYtData('flask',10)
		api=str(type(_api))		
		self.assertTrue( api == "<class 'pyytdata.pyytdata.PyYtData'>") 
		# for checking equality we have to override __eq__ builtin of object which is avoided by this kind of builshit 
				
	def test_check_google_application_credential_env(self):
		self.assertTrue(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')!=None)

		
if __name__=='__main__':
	unittest.main()
