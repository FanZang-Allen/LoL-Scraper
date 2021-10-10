import json
import string


def export_to_json(file_path, export_dict):
    with open(file_path, 'w') as export_file:
        json.dump(export_dict, export_file, indent=2)
        print("data has been export to " + file_path)


def load_json(file_path):
    with open(file_path) as loaded_file:
        data = json.load(loaded_file)
        return data

