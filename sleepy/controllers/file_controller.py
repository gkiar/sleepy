import connexion
import six

from sleepy.models.obj import Obj  # noqa: E501
from sleepy import util


def get_files(schema):  # noqa: E501
    """Get file pointers to data

    Accepts arbitrary queries compliant with the data schema # noqa: E501

    :param schema: Name of the data schema being used for the query
    :type schema: str

    :rtype: List[Obj]
    """
    return 'do some magic!'
