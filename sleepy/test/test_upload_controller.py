# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from sleepy.models.api_response import ApiResponse  # noqa: E501
from sleepy.test import BaseTestCase


class TestUploadController(BaseTestCase):
    """UploadController integration test stubs"""

    def test_upload_data(self):
        """Test case for upload_data

        uploads an image
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/sleepy/upload',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
