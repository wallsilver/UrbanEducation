import inspect
from pprint import pprint

def introspection_info(obj):
    obj_info = {}
#    metod_obj = type(obj)
    obj_info = {'type':type(obj), 'ID':id(obj), 'attrib':inspect.getmembers(obj.__getattribute__), 'methods':dir(obj),}
#    metod_obj = dir(obj)
#    type(metod_obj)
#    type_obj = type(obj)
#    type(type_obj)
#    return (type_obj, metod_obj)
    return obj_info





number_info = introspection_info(42)
pprint(number_info,)