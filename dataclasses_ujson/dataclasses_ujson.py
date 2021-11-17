from dataclasses import is_dataclass
import sys
from typing import Any, Generator, TypeVar, Type, Union

NEW_TYPING = sys.version_info[:3] >= (3, 7, 0)  # PEP 560
if NEW_TYPING:
    from typing import _GenericAlias as GenericMeta
else:
    from typing import GenericMeta

import ujson as json

DC = TypeVar('DC')
DC_GENERATOR = Generator[Type[DC], None, None]


class UJsonMixin:

    @classmethod
    def loads(cls: DC, json_string: str, many: bool = False,
              **kwargs) -> Union[Type[DC], DC_GENERATOR]:
        """

        :param json_string: string of json, what should be encoded
        :param many: true if it is list. For example: [{"x": 1}, {"x": 2}]
        :param kwargs: other arguments to json.loads
        :return: Union[DC, DC_GENERATOR]
        """
        data = json.loads(json_string, **kwargs)
        if many:
            return UJsonMixin.from_dict_many(cls, data)
        return UJsonMixin.from_dict(cls, data)

    def dumps(self):
        raise NotImplemented()

    @staticmethod
    def from_dict(cls: DC, data: dict, _kwargs: dict = None) -> Type[DC]:
        if _kwargs is None:
            _kwargs = {}
        try:
            for field in getattr(cls, '__dataclass_fields__').values():
                field_value = data.get(field.name)
                if field_value is None:
                    _kwargs[field.name] = None
                    continue
                if (field.type is str or field.type is float or field.type is int
                        or field.type is bool):
                    _kwargs[field.name] = field_value
                elif UJsonMixin._is_collection(field.type):
                    _kwargs[field.name] = UJsonMixin._decode_collection(field.type,
                                                                        field_value)
                elif is_dataclass(field.type):
                    _kwargs[field.name] = UJsonMixin.from_dict(field.type, field_value)
                else:
                    _kwargs[field.name] = field_value
        except AttributeError:
            raise TypeError('must be called with a dataclass type or instance')
        return cls(**_kwargs)

    @staticmethod
    def from_dict_many(cls: DC, data: list) -> DC_GENERATOR:
        for d in data:
            yield UJsonMixin.from_dict(cls, d)

    @staticmethod
    def _is_collection(obj_type: Any) -> bool:
        simple_type = False
        if isinstance(obj_type, str):
            return False
        try:
            simple_type = obj_type is list or obj_type is dict
        except AttributeError:
            pass
        if simple_type:
            return True
        else:
            return type(obj_type) is GenericMeta

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

        if is_dataclass(type_arg) and type_value is not list:
            return UJsonMixin.from_dict(type_arg, value)
        if is_dataclass(type_arg) and type_value is list:
            return UJsonMixin.from_dict_many(type_arg, value)
        else:
            return value
