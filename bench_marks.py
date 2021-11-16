import time
import json

from dataclasses import dataclass
from dataclasses_ujson.dataclasses_ujson import UJsonMixin
from dataclasses_json import DataClassJsonMixin
import ujson

DICT_JSON = """
{
    "_id": "5af284b8ebc5ca7f9ec9c5b0",
    "index": 0,
    "guid": "dc5ab840-2cf8-44f3-9944-c8303a84524c",
    "isActive": false,
    "balance": "$2,392.56",
    "picture": "http://placehold.it/32x32",
    "age": 39,
    "eyeColor": "green",
    "name": "Catherine Moon",
    "gender": "female",
    "company": "ZILLACON",
    "email": "catherinemoon@zillacon.com",
    "phone": "+1 (917) 404-2234",
    "address": "666 Chauncey Street, Waterford, Massachusetts, 9953",
    "about": "Quis sit fugiat ad sunt do cillum pariatur occaecat Lorem amet excepteur irure elit non. Cupidatat reprehenderit magna ex nulla voluptate sit ex Lorem voluptate eu enim sit commodo duis. Nulla aliqua incididunt veniam sint velit sit anim consectetur elit ut commodo in. Qui amet minim ad ad consequat dolore incididunt amet ipsum nostrud et consectetur. Ullamco in sit aliquip aute nostrud quis exercitation incididunt nostrud. Culpa commodo veniam incididunt est.",
    "registered": "2017-12-19T07:08:18 -07:00",
    "latitude": 8.699908,
    "longitude": 28.591773,
    "greeting": "Hello, Catherine Moon! You have 1 unread messages.",
    "favoriteFruit": "apple"
  }
"""
LIST_JSON = "[{}]".format(DICT_JSON)


@dataclass(frozen=True)
class DictUJson(UJsonMixin):
    _id: str
    index: int
    guid: str
    isActive: bool
    balance: str
    picture: str
    age: int
    eyeColor: str
    name: str
    gender: str
    company: str
    email: str
    phone: str
    address: str
    about: str
    registered: str
    latitude: float
    longitude: float
    greeting: str
    favoriteFruit: str

@dataclass(frozen=True)
class DictJson(DataClassJsonMixin):
    _id: str
    index: int
    guid: str
    isActive: bool
    balance: str
    picture: str
    age: int
    eyeColor: str
    name: str
    gender: str
    company: str
    email: str
    phone: str
    address: str
    about: str
    registered: str
    latitude: float
    longitude: float
    greeting: str
    favoriteFruit: str


if __name__ == "__main__":
    count = 100000

    def measure(json_string, many=False):
        perf_counter = {
            "json": 0,
            "ujson": 0,
            "udata_class": 0,
            "data_class": 0,
        }

        t = time.process_time()
        for i in range(count):
            DictUJson.loads(json_string, many=many)
        perf_counter["udata_class"] = time.process_time() - t

        t = time.process_time()
        for i in range(count):
            ujson.loads(json_string)
        perf_counter["ujson"] = time.process_time() - t

        t = time.process_time()
        for i in range(count):
            json.loads(json_string)
        perf_counter["json"] = time.process_time() - t

        try:
            t = time.process_time()
            for i in range(count):
                DictJson.from_json(json_string)
            perf_counter["data_class"] = time.process_time() - t
        except TypeError:
            perf_counter["data_class"] = "None"
        except AttributeError:
            perf_counter["data_class"] = "None"

        for key in perf_counter:
            print("{}: {}s".format(key, perf_counter[key]))


    measure(DICT_JSON)
    measure(LIST_JSON, many=True)