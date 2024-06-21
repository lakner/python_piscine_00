
def NULL_not_found(object: any) -> int:

    name = "Type not Found"
    if object is None:
        name = "Nothing"
    elif (isinstance(object, float) and object != object):
        name = "Cheese"
    elif (isinstance(object, int) and not object):
        name = "Zero"
    elif (isinstance(object, str) and not object):
        name = "Empty"
    elif (isinstance(object, bool) and not object):
        name = "Fake"
    else:
        print(name)
        return 1

    print(f"{name}: object {type(object)}")
    return 0
