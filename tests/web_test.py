import unittest
try:
    from app import app
except ImportError:
    import sys
    import os.path
    sys.path.append(os.path.abspath('.'))
    from app import app


class WebTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.debug = True

    def sms(self, body, path='/sms', number='+15555555555'):
        params = {
            'SmsSid': 'SMtesting',
            'AccountSid': 'ACtesting',
            'From': number,
            'To': '+16666666666',
            'Body': body,
            'ApiVersion': '2010-04-01',
            'Direction': 'inbound'}
        return self.app.post(path, data=params)

   
class Test_Sms(WebTest):
    def test_sms(self):
        response = self.sms("Testing.")
        self.assertTwiML(response)
        self.assertTrue(":" in response.data, "Did not find " \
                "a preface colon in response: %s" % response.data)

    def test_smsHelp(self):
        response = self.sms("help")
        self.assertTwiML(response)
        self.assertTrue("GIMME" in response.data, "Did not find " \
                "GIMME in response: %s" % response.data)


class Test_Web(WebTest):
    def test_index(self):
        response = self.app.get('/')
        self.assertTrue("</html>" in response.data, "Did not find " \
                "html tag close in response: %s" % response.data)

    def test_reaction(self):
        response = self.app.get('/reaction')
        self.assertTrue("</html>" in response.data, "Did not find " \
                "html tag close in response: %s" % response.data)


if __name__ == '__main__':
    unittest.main()
