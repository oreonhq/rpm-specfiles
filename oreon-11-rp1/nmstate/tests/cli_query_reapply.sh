#!/bin/bash -ex

TMP_FILE=$(mktemp /tmp/nmstate.XXXXXX.yaml)

nmstatectl show > $TMP_FILE

cat $TMP_FILE

nmstatectl set $TMP_FILE 2>&1
