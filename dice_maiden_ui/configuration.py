import jsonschema
import json


def validate_config_against_schema(config_json):
    with open('../data/configuration.schema') as f:
        schema_json = json.load(f)

    jsonschema.validate(config_json, schema_json)
