def pour_coffee(size):
    size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20
    }
    return size_to_ounce_map.get(size)
    # return size_to_ounce_map.get(size, "Please enter a valid cup size.")

pour_coffee("jumbo")

# dict.items()
my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}
[item for item in my_dict.items()] # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
[key for key in my_dict] # ['a', 'b', 'c', 'd']
[my_dict[key] for key in my_dict] # [1, 2, 3, 4]
