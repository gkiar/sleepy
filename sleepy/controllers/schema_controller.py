import connexion
import six

from sleepy.models.obj import Obj  # noqa: E501
from sleepy import util


def get_schema(schema):  # noqa: E501
    """Get a data schema

    Accepts name of an installed data schema to return # noqa: E501

    :param schema: Name of the data schema to return
    :type schema: str

    :rtype: List[Obj]
    """
    return 'do some magic!'
