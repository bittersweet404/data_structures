#!/usr/bin/env python3


def create_dict():
    d = {"a": 1, "b":2}
    d_nested = {"a": {"a":1,"b":2,"c":3}, "b":3, "k":67}
    return d, d_nested

d, d_nested = create_dict()


def dict_operation(d):
    print("original dict:", d)
    d["h"]={"l":787}
    print("append h :",d)
    print("D.pop('k')", d.pop("k"))
    print("D.get('b')", d.get("b"))

    del d['b']
    print("del d['b']", d)

    x=d.popitem()
    print("popitem arbitary element", x, d)

    d.update({1:2})
    print("d.update({1:2})", d)

dict_operation(d_nested)
