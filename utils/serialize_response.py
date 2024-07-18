import cattr
from typing import Type
from requests import Response


def structure_response(response: Response, type_response: Type) -> object:
    """
    convert the response json to class object
    :param response: response
    :param type_response: type response
    :return: modify the response to given response type
    """
    return cattr.structure(response.json(), type_response)