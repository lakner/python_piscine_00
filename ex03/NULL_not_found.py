
def NULL_not_found(object: any) -> int:

    name = "Type not Found"
    if object is None:
        name = "Nothing"
    elif (isinstance(object, float)):
        name = "Cheese"
    elif (isinstance(object, int)):
        name = "Zero"
    elif (isinstance(object, str) and object != "Brian"):
        name = "Empty"
    elif (isinstance(object, bool)):
        name = "Fake"
    else:
        print(name)
        return 1

    print(f"{name}: {type(object)}")
    return 1
