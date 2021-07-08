import jsonschema
import json
import os


def validate_config_against_schema(config_json):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'configuration.schema')

    with open(file_path) as f:
        schema_json = json.load(f)

    jsonschema.validate(config_json, schema_json)
