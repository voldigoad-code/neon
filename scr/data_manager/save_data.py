import json

def save_data(dict, path, mode="w"):
    json_object = json.dumps(dict, indent=4)
    with open(path, mode) as outfile:
        outfile.write(json_object)