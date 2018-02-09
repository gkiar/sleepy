import connexion
import six

from sleepy.models.obj import Obj  # noqa: E501
from sleepy import util


def query_data(schema):  # noqa: E501
    """Learn information about data

    Accepts arbitrary queries compliant with the data schema # noqa: E501

    :param schema: Name of the data schema being used for the query
    :type schema: str

    :rtype: List[Obj]
    """
    return 'do some magic!'
