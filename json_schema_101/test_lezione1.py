from lezione1 import schema
from jsonschema import validate

def test_json():
    assert validate_wrapper(instance={"name" : "Eggs", "price" : 34.99}, schema=schema) == True

def validate_wrapper(instance, schema):
    try:
        validate(instance, schema)
        return True
    except:
        return False
