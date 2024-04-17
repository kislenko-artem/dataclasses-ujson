from tests import (JsonList, JsonSimple, JsonDict, JsonNoTypingList,
                   JsonNoTypingDict, JsonNested, JsonUnion, JsonListNested,
                   JsonSimpleOptional, JsonSimpleNotOptional, JsonSimpleSkip,
                   JSON_SIMPLE, JSON_LIST, JSON_DICT, JSON_NESTED,
                   JSON_UNION_V1, JSON_UNION_V2, JSON_SIMPLE_LIST,
                   JSON_NESTED_LIST, JSON_SIMPLE_OPTIONAL)


class TestLoadsDict:
    def test_simple(self):
        x1 = JsonSimple.loads(JSON_SIMPLE).x
        x2 = JsonSimple(x=1).x
        assert x1 == x2

    def test_nested_list(self):
        x1 = JsonList.loads(JSON_LIST).x
        x2 = JsonList(x=[1]).x
        assert x1 == x2

    def test_nested_dict(self):
        x1 = JsonDict.loads(JSON_DICT).x
        x2 = JsonDict(x={"d": 1}).x
        assert x1 == x2

    def test_no_typing_list(self):
        x1 = JsonNoTypingList.loads(JSON_LIST).x
        x2 = JsonNoTypingList(x=[1]).x
        assert x1 == x2

    def test_no_typing_dict(self):
        x1 = JsonNoTypingDict.loads(JSON_DICT).x
        x2 = JsonNoTypingDict(x={"d": 1}).x
        assert x1 == x2

    def test_nested_dataclasses(self):
        d1 = JsonNested.loads(JSON_NESTED)
        d2 = JsonNested(a=JsonSimple(x=1), b=JsonList(x=[1]),
                        c=JsonNoTypingDict(x={"d": 1}))
        assert d1.a == d2.a
        assert d1.b == d2.b
        assert d1.c == d2.c

    def test_union_v1(self):
        d1 = JsonUnion.loads(JSON_UNION_V1)
        d2 = JsonUnion(a=1, b={"x": [1]}, c={"x": [1]})
        assert d1.a == d2.a
        assert d1.b == d2.b
        assert d1.c == d2.c

    def test_union_v2(self):
        d1 = JsonUnion.loads(JSON_UNION_V2)
        d2 = JsonUnion(a="s", b={"x": {"d": 1}}, c={"x": {"d": 1}})
        assert d1.a == d2.a
        assert d1.b == d2.b
        assert d1.c == d2.c


class TestLoadsMany:

    def test_simple(self):
        x1 = JsonSimple.loads(JSON_SIMPLE_LIST, many=True)
        x2 = JsonSimple(x=1)
        assert list(x1) == [x2]

    def test_nested(self):
        d1 = JsonListNested.loads(JSON_NESTED_LIST)
        d2 = JsonListNested(a=JsonSimple(x=1), b=[JsonList(x=[1])],
                            c=[JsonNoTypingDict(x={"d": 1})])
        assert d1.a == d2.a
        assert list(d1.b)[0].x == d2.b[0].x
        assert list(d1.c)[0].x == d2.c[0].x


class TestOptional:
    def test_simple(self):
        x1 = JsonSimpleOptional.loads(JSON_SIMPLE_OPTIONAL)
        x2 = JsonSimpleOptional(x=1, y=None)
        assert x1.y == x2.y

    def test_simple_err(self):
        try:
            JsonSimpleNotOptional.loads(JSON_SIMPLE_OPTIONAL)
        except ValueError:
            pass
        else:
            raise Exception("wait for Exception")


class TestToSerializable:
    def test_simple(self):
        d1 = JsonSimple.loads(JSON_SIMPLE)
        new_dict = d1.to_serializable()
        assert type(new_dict) == dict
        assert new_dict == {"x": 1}

    def test_skip(self):
        d1 = JsonSimpleSkip(x=1, _x=2)
        new_dict = d1.to_serializable(delete_private=True)
        assert type(new_dict) == dict
        assert new_dict == {"x": 1}

    def test_no_skip(self):
        d1 = JsonSimpleSkip(x=1, _x=2)
        new_dict = d1.to_serializable()
        assert type(new_dict) == dict
        assert new_dict == {"x": 1, "_x": 2}
