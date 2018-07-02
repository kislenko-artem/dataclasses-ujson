from typing import List, Dict, Union, Optional

from dataclasses import dataclass
from dataclasses_ujson.dataclasses_ujson import UJsonMixin

JSON_SIMPLE = '{"x": 1}'
JSON_SIMPLE_OPTIONAL = '{"x": 1, "y": null}'
JSON_LIST = '{"x": [1]}'
JSON_DICT = '{"x": {"d": 1}}'
JSON_NESTED = '{{"a": {simple}, "b": {list}, "c": {dict}}}'.format(
    simple=JSON_SIMPLE, list=JSON_LIST, dict=JSON_DICT)
JSON_UNION_V1 = '{{"a": 1, "b": {list}, "c": {list}}}'.format(list=JSON_LIST)
JSON_UNION_V2 = '{{"a": "s", "b": {dict}, "c": {dict}}}'.format(dict=JSON_DICT)

JSON_SIMPLE_LIST = '[{"x": 1}]'
JSON_NESTED_LIST = '{{"a": {simple}, "b": [{list}], "c": [{dict}]}}'.format(
simple=JSON_SIMPLE, list=JSON_LIST, dict=JSON_DICT)


@dataclass(frozen=True)
class JsonList(UJsonMixin):
    x: List[int]


@dataclass(frozen=True)
class JsonSimple(UJsonMixin):
    x: int


@dataclass(frozen=True)
class JsonDict(UJsonMixin):
    x: Dict[str, int]


@dataclass(frozen=True)
class JsonNoTypingDict(UJsonMixin):
    x: dict


@dataclass(frozen=True)
class JsonNoTypingList(UJsonMixin):
    x: list


@dataclass(frozen=True)
class JsonNested(UJsonMixin):
    a: JsonSimple
    b: JsonList
    c: JsonNoTypingDict


@dataclass(frozen=True)
class JsonUnion(UJsonMixin):
    a: Union[str, int]
    b: Union[dict, list]
    c: Union[Dict[str, int], List[int]]


@dataclass(frozen=True)
class JsonListNested(UJsonMixin):
    a: JsonSimple
    b: List[JsonList]
    c: List[JsonNoTypingDict]

@dataclass(frozen=True)
class JsonSimpleOptional(UJsonMixin):
    x: int
    y: Optional[int]