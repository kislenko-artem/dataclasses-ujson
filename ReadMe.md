# JSON with DataClasses 

The library provides a simple API for decoding JSON to dataclasses.
You can use nested dataclasses. The library uses `ujson` for better performance.
You need install [dataclasses](https://github.com/ericvsmith/dataclasses) for python3.6

### Examples

```python
from typing import List, Dict
from dataclasses import dataclass
from dataclasses_ujson.dataclasses_ujson import UJsonMixin

json_string = """
{"a": 1, "b": [{"x": 1}, {"x": 2}], "c": {"x": 1}}
"""

@dataclass(frozen=True)
class JsonDict(UJsonMixin):
    x: Dict[str, int]

@dataclass(frozen=True)
class JsonClass(UJsonMixin):
    a: int
    b: List[JsonDict]
    c: Dict[str, int]

data = JsonClass.loads(json_string)

print(data.c["x"])
print(list(data.b)[0].x)

```

All lists will be returned as generators

```python
from typing import List, Dict
from dataclasses import dataclass
from dataclasses_ujson.dataclasses_ujson import UJsonMixin

json_string = """
[{"x": 1}, {"x": 2}]
"""

@dataclass(frozen=True)
class JsonDict(UJsonMixin):
    x: Dict[str, int]

data = JsonDict.loads(json_string, many=True)

print(data) # generator object UJsonMixin
print(list(data)) # list of JsonDict

```

### Performance:

Libraries were compared:

* The default library `json` of python
* The library `ujson` https://github.com/esnme/ultrajson
* The library `dataclasses-json` https://github.com/lidatong/dataclasses-json

The script is placed in repository (bench_marks.py):


|Name of library|Results|
|---------------|-------|
|json           |1.4237859140000007s|
|ujson          |0.8745695059999998s|
|dataclasses-ujson    |3.316673846s|
|dataclasses-json    |20.831920666000002s|

if generator will be returned (using flag many=true)

|Name of library|Results|
|---------------|-------|
|json           |1.4263252840000007s|
|ujson          |0.8816592850000013s|
|dataclasses-ujson    |1.0314886600000008s|
|dataclasses-json    |-|

