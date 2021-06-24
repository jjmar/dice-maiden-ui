from jsonschema import validate, exceptions
import json


def open_json_file(path):
    with open(path) as f:
        schema = json.load(f)

    return schema


def validate_json_schema(schema, config):
    try:
        validate(config, schema)
    except exceptions.ValidationError as e:
        print(e.message)
        raise


def get_config():
    config = open_json_file('../data/configuration.schema')
    schema = open_json_file('../documentation/config_example.json')

    validate_json_schema(schema, config)

    return schema
