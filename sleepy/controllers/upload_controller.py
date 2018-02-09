import connexion
import six

from sleepy.models.api_response import ApiResponse  # noqa: E501
from sleepy import util


def upload_data(file=None):  # noqa: E501
    """uploads an image

     # noqa: E501

    :param file: file to upload
    :type file: werkzeug.datastructures.FileStorage

    :rtype: ApiResponse
    """
    return 'do some magic!'
