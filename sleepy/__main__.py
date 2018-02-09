#!/usr/bin/env python3

from argparse import ArgumentParser
from jsonschema import validate, ValidationError
import connexion
import json
import os

from sleepy import encoder


def main():
    parser = ArgumentParser()
    parser.add_argument("schema", action="store")
    parser.add_argument("datadir", action="store")
    results = parser.parse_args()

    schema = results.schema
    datadir = results.datadir

    try:
        schema = json.load(open(schema))
    except Exception as e:
        print("Failed to load shema!")
        raise e

    if not os.path.isdir(datadir):
        raise SystemExit("Invalid data directory")

    try:
        datasets = [fil for fil in os.listdir(datadir) if fil.endswith('.json')]
        for dataset in datasets:
            with open(os.path.join(datadir, dataset)) as fhandle:
                data_json = json.load(fhandle)
                [validate(schema, data_obj) for data_obj in data_json]
    except Exception as e:
        print("Failed to validate data files!")
        raise e

    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Sleepy'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
