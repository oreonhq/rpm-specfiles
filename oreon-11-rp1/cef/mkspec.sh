#!/bin/sh

api_versions="$1"

for api in $(jq -r <"$api_versions" '.hashes | keys[]'); do
    echo "Provides: cef(api) = $api"
done
