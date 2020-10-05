import pytest
from tests.data.snake_oil_data import ensembles_response


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.data = data
            self.status_code = status_code

        def json(self):
            return self.data

        def text(self):
            return self.data

    if args[0] in ensembles_response:
        return MockResponse(ensembles_response[args[0]], 200)
    return MockResponse({}, 400)
