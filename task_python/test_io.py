import json


def test_io():
    with open('data', 'r') as file:
        a = file.read()
        result = json.loads(a.replace("\\n", ""))
        result.update({"b": 2})
    with open('data', 'w') as file:
        file.write(json.dumps(result))

# \n\n\n{"a":\n\n\n{"b"\n: 1}}