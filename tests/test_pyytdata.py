from pyytdata.pyytdata import PyYtData
import os

import unittest


class TestPyYtData(unittest.TestCase):
    def test_check_env(self):
        self.assertTrue(os.environ.get("API_KEY") != None)

    def test_apiall(self):
        _api = PyYtData("flask", 10)
        api = str(type(_api))
        self.assertTrue(api == "<class 'pyytdata.pyytdata.PyYtData'>")
        # for checking equality we have to override __eq__ builtin of object which is avoided by this kind of builshit

    def test_check_google_application_credential_env(self):
        self.assertTrue(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") != None)
    
    def test_functions_of_the_class(self):
        api = PyYtData("flask", 10)
        data=api.get_titles()
        data2=api.get_descriptions()
        data3=api.get_image_urls()
        data4=api.get_links()
        self.assertTrue(type(data)==list)
        self.assertTrue(type(data4)==list)
        self.assertTrue(type(data2)==list)
        self.assertTrue(type(data3)==list)
        self.assertTrue(len(data)==10)
        
if __name__ == "__main__":
    unittest.main()
