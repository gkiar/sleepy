# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from sleepy.models.obj import Obj  # noqa: E501
from sleepy.test import BaseTestCase


class TestQueryController(BaseTestCase):
    """QueryController integration test stubs"""

    def test_query_data(self):
        """Test case for query_data

        Learn information about data
        """
        query_string = [('schema', 'schema_example')]
        response = self.client.open(
            '/sleepy/query',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
