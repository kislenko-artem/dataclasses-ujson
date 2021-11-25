from dataclasses import is_dataclass
from typing import (Any, Generator, TypeVar, Type, Union, _GenericAlias as GenericMeta,
                    _UnionGenericAlias as UnionGenericAlias)

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
                if field_value is None and UJsonMixin._is_optional(field.type):
                    _kwargs[field.name] = None
                    continue
                try:
                    if field.type is str:
                        _kwargs[field.name] = str(field_value)
                    elif field.type is float:
                        _kwargs[field.name] = float(field_value)
                    elif field.type is int:
                        _kwargs[field.name] = int(field_value)
                    elif field.type is bool:
                        _kwargs[field.name] = bool(field_value)
                    elif UJsonMixin._is_optional(field.type):
                        if is_dataclass(field.type.__args__[0]):
                            _kwargs[field.name] = UJsonMixin.from_dict(field.type.__args__[0], field_value)
                        else:
                            _kwargs[field.name] = field_value
                    elif UJsonMixin._is_collection(field.type):
                        _kwargs[field.name] = UJsonMixin._decode_collection(field.type,
                                                                            field_value)
                    elif is_dataclass(field.type):
                        _kwargs[field.name] = UJsonMixin.from_dict(field.type, field_value)
                    else:
                        _kwargs[field.name] = field_value
                except ValueError as e:
                    raise ValueError('ValueError: {}; field: {}, value: {}, type: {}.'.format(
                        e, field.name, field_value, field.type))
        except AttributeError as e:
            raise TypeError('must be called with a dataclass type or instance: {}'.format(e))
        return cls(**_kwargs)

    @staticmethod
    def from_dict_many(cls: DC, data: list) -> DC_GENERATOR:
        for d in data:
            yield UJsonMixin.from_dict(cls, d)

    @staticmethod
    def _is_optional(obj_type: Any) -> bool:
        if isinstance(obj_type, UnionGenericAlias) and len(obj_type.__args__) == 2 \
                and obj_type.__args__[1] == type(None):
            return True
        return False

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
