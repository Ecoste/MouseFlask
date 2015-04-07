__author__ = 'A pen is a pen'

import os
import server
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()
        server.init_db()

    def tearDown(self):
        pass

    def receivePoints(self, get):
        return self.app.get('/receiveData/{}'.format(get), method=['GET'])

    def sendPoints(self, points):
        return self.app.post('/sendData/{}'.format(points), method=['POST'])

    def test_sendReceivePoints(self):
        rv = self.sendPoints("6,2C1,4C7,3C0,1C8,2C6,1C4,7")
        assert "Done" in rv.data.decode("utf-8")
        rv = self.receivePoints("0=0")
        assert "6,2C1,4C7,3C0,1C8,2C6,1C4,7" in rv.data.decode("utf-8")
        rv = self.receivePoints("{}=3".format(self.receiveUID().data.decode('utf-8')))
        assert "7,3C0,1C8,2C6,1C4,7" in rv.data.decode("utf-8")

    def receiveUID(self):
        return self.app.get('/receiveUID', method=['GET'])

    def test_receiveUID(self):
        t = [self.receiveUID().data.decode("utf-8")] * 1000
        assert len(t)!= len(set(t))

if __name__ == '__main__':
    unittest.main()