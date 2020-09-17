import os
import unittest

from pyytdata import PyYtData

class TestPyYtData(unittest.TestCase):

    def test_check_env(self):
        self.assertTrue(os.environ.get('API_KEY') != None)

    def setUp(self):
        self.data = PyYtData('flask', 1)
        self.rslt = self.data.get_videoinfo()

    def test_get_videoinfo(self):
        self.assertTrue(len(self.rslt) == 1)

    def test_get_title(self):
        self.assertTrue(self.rslt[0].get_title() == 'Learn Flask for Python - Full Tutorial')

    def test_get_description(self):
        self.assertTrue(self.rslt[0].get_description() == 'Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. Learn how to use it ...')

    def test_get_image_url(self):
        self.assertTrue(self.rslt[0].get_image_url() == 'https://i.ytimg.com/vi/Z1RJmh_OqeA/mqdefault.jpg')

    def test_get_link(self):
        self.assertTrue(self.rslt[0].get_link() == 'https://www.youtube.com/watch?v=Z1RJmh_OqeA')

    def test_get_publishedtime(self):
        pass


if __name__ == '__main__':
    unittest.main()
