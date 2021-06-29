import jsonschema
import json


def open_json_file(path):
    with open(path) as f:
        data = json.load(f)

    return data


def validate_config_against_schema(config_json):
    schema_json = open_json_file('../data/configuration.schema')

    jsonschema.validate(config_json, schema_json)

