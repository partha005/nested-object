def get_value(obj, key):
    keys = key.split('/')
    value = object
    for key in keys:
        value = value[key]
    return value

object = {"a":{"b":{"c":"d"}}}
key = "a/b/c"
print(get_value(object, key))
