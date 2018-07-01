from typing import Any, Generator, List, Union

import ujson as json
from dataclasses import is_dataclass, fields, dataclass

DC = dataclass
DC_GENERATOR = Generator[List[DC], List[DC], None]


class UJsonMixin:

    @classmethod
    def loads(cls: DC, json_string: str, many: bool=False,
              **kwargs) -> Union[DC, DC_GENERATOR]:
        """

        :param json_string: string of json, what should be encoded
        :param many: true if it is list. For example: [{"x": 1}, {"x": 2}]
        :param kwargs: other arguments to json.loads
        :return: Union[DC, DC_GENERATOR]
        """
        data = json.loads(json_string, **kwargs)
        if many:
            return UJsonMixin._loads_many(cls, data)
        return UJsonMixin._loads(cls, data)

    def dumps(self):
        raise NotImplemented()

    @staticmethod
    def _loads(cls: DC, data: dict, _kwargs: dict = None) -> DC:
        if _kwargs is None:
            _kwargs = {}
        for field in fields(cls):
            field_value = data[field.name]
            if field.type in [str, float, int, bool]:
                _kwargs[field.name] = field_value
            elif UJsonMixin._is_collection(field.type):
                _kwargs[field.name] = UJsonMixin._decode_collection(field.type,
                                                                    field_value)
            elif is_dataclass(field.type):
                _kwargs[field.name] = UJsonMixin._loads(field.type, field_value)
            else:
                _kwargs[field.name] = field_value
        return cls(**_kwargs)

    @staticmethod
    def _loads_many(cls: DC, data: list) -> DC_GENERATOR:
        for d in data:
            yield UJsonMixin._loads(cls, d)

    @staticmethod
    def _is_collection(obj_type: Any) -> bool:
        if obj_type == str:
            return False
        try:
            return obj_type == list or obj_type == dict
        except AttributeError:
            pass
        return False

    @staticmethod
    def _decode_collection(obj_type: Any, value):
        if not value:
            return value
        try:
            if obj_type.__args__ is None:
                return value
            type_arg = obj_type.__args__[0]
        except AttributeError:
            return value
        type_value = type(value)

        if is_dataclass(type_arg) and type_value != list:
            return UJsonMixin._loads(type_arg, value)
        if is_dataclass(type_arg) and type_value == list:
            return UJsonMixin._loads_many(type_arg, value)
        else:
            return value
