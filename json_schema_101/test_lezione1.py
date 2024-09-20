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

frutti = """
frutta, prezzo, kg
mele, 1, 2
pere, 2, 3
banane, 2, 4
ananas, 2, 3
"""

def test_snapshot(snapshot):
    snapshot.snapshot_dir = 'snapshot'
    snapshot.assert_match(frutti, "output.txt")


