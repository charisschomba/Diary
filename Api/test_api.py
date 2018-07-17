import unittest,json
from run import app
"""
testing my api
"""

class TestApp(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_get_items(self):
        response = self.tester.get('/mydiary/api/v1/entries')
        self.assertEqual(response.status_code, 200)
        self.assertIn('', str(response.data))
        self.assertIn('application/json', str(response.headers))

    def test_post_method(self):
        payload = {'title':'off day','content':'Going to watch football'}
        response = self.tester.post('/mydiary/api/v1/entries',data=json.dumps(payload),
        content_type="application/json")
        self.assertEquals(response.status_code,201)
        response_message = json.loads(response.data.decode('utf8'))
        self.assertEqual("Going to watch football",response_message['content'])
