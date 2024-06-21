def all_thing_is_obj(object: any) -> int:

    # I don't know why this is in the example output, but we need to print type not found for integers
    if (isinstance(object, int)):
        print("Type not found")
    elif (isinstance(object, str)):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    return (42)

