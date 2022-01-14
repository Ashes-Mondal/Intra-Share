import json
def encodeJSON(input: dict):
    return str(json.dumps(input)).encode()