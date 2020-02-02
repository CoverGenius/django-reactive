#!/usr/bin/env bash

DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
ROOT=$DIR/..
DIST_DIR=${ROOT}/django_reactive/static/dist

curl --request GET -sL \
  --url 'https://unpkg.com/react@16/umd/react.production.min.js' \
  --output "${DIST_DIR}/react.js"

curl --request GET -sL \
  --url 'https://unpkg.com/react-dom@16/umd/react-dom.production.min.js' \
  --output "${DIST_DIR}/react-dom.js"

curl --request GET -sL \
  --url 'https://unpkg.com/react-jsonschema-form@1.8/dist/react-jsonschema-form.js' \
  --output "${DIST_DIR}/react-jsonschema-form.js"

curl --request GET -sL \
  --url 'https://unpkg.com/react-jsonschema-form@1.8/dist/react-jsonschema-form.js.map' \
  --output "${DIST_DIR}/react-jsonschema-form.js.map"
