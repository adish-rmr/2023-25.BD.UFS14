from functions import open_data

def ingredient_dict_test(x):
    assert type(x) == dict

ingredient_dict_test(open_data())