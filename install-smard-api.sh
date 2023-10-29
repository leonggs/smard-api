#!/usr/bin/env bash

set -x

rm -rf python-client

docker run --rm -v ${PWD}:/local \
    openapitools/openapi-generator-cli generate -i /local/openapi.yaml -g python -c /local/generator_config.yaml -o /local/python-client 

python python-client/rename_generated_code.py

pip install poetry

cd python-client

poetry build

pip install -U ./dist/de_smard-0.1.0.tar.gz