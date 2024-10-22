from functions import open_data
from jsonschema import validate
from functions import x, schema

def test_ingredient_dict():
    x = open_data()
    assert type(x) == dict

def validate_json():
    try:
        validate(x, schema)
        return True
    except:
        return False

print(validate_json())

def test_snapshot(snapshot):
    diz = str(open_data())
    snapshot.snapshot_dir = 'snapshot'
    snapshot.assert_match(diz, "ingredients.txt")

