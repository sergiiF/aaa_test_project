import flexmock
import json

from cp_test_project.tests import FunctionalTest
from cp_test_project.controllers import root


class TestRootController(FunctionalTest):

    def test_get(self):
        response = self.app.get('/')
        assert response.status_int == 200

    def test_search(self):
        response = self.app.post('/', params={'q': 'RestController'})
        assert response.status_int == 302
        assert response.headers['Location'] == (
            'http://pecan.readthedocs.org/en/latest/search.html'
            '?q=RestController'
        )

    def test_get_not_found(self):
        response = self.app.get('/a/bogus/url', expect_errors=True)
        assert response.status_int == 404

    def test_hello(self):
        flexmock.flexmock(root, hello='qwerty')
        response = self.app.get('/hello.json?name=you')
        body = json.loads(response.body)

        assert response.status_int == 200
        assert body['response'] == 'qwerty'
