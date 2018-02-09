# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from sleepy.models.obj import Obj  # noqa: E501
from sleepy.test import BaseTestCase


class TestFileController(BaseTestCase):
    """FileController integration test stubs"""

    def test_get_files(self):
        """Test case for get_files

        Get file pointers to data
        """
        query_string = [('schema', 'schema_example')]
        response = self.client.open(
            '/sleepy/file',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
