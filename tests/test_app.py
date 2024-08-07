import unittest
from app import app
import json

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Intrusion Detection System Dashboard', result.data)

    def test_stats(self):
        result = self.app.get('/stats')
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.data)
        self.assertIn('total_packets', data)
        self.assertIn('udp_traffic', data)
        self.assertIn('tcp_traffic', data)
        self.assertIn('alerts', data)

    def test_control(self):
        payload = {'new_setting': 'value'}
        result = self.app.post('/control', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.data)
        self.assertEqual(data['status'], 'Settings updated successfully')

if __name__ == '__main__':
    unittest.main()
