# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Pet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, tag=None):  # noqa: E501
        """Pet - a model defined in OpenAPI

        :param id: The id of this Pet.  # noqa: E501
        :type id: int
        :param name: The name of this Pet.  # noqa: E501
        :type name: str
        :param tag: The tag of this Pet.  # noqa: E501
        :type tag: str
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'tag': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'tag': 'tag'
        }

        self._id = id
        self._name = name
        self._tag = tag

    @classmethod
    def from_dict(cls, dikt) -> 'Pet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pet of this Pet.  # noqa: E501
        :rtype: Pet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Pet.


        :return: The id of this Pet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pet.


        :param id: The id of this Pet.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Pet.


        :return: The name of this Pet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pet.


        :param name: The name of this Pet.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tag(self):
        """Gets the tag of this Pet.


        :return: The tag of this Pet.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Pet.


        :param tag: The tag of this Pet.
        :type tag: str
        """

        self._tag = tag
