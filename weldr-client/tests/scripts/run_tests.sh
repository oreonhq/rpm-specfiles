#!/bin/bash
set -eux

FAILANY=0

function fail {
    echo -e "\n\n#### ERROR: $1\n"
    FAIL=1
    FAILANY=1
}

function status {
    if [ "$FAIL" -eq 0 ]; then
        echo -e "\n\n#### PASS: $1\n"
    else
        echo -e "\n\n#### FAIL: $1\n"
    fi
}

function running {
    FAIL=0
    echo -e "\n\n#### RUN: $1\n"
}

backend_start() {
    export BACKEND="osbuild-composer"
    systemctl start osbuild-composer.socket
    RET=$?

    if [ "$RET" -eq 0 ]; then
        # wait for the backend to become ready
        tries=0
        until curl -m 15 --unix-socket /run/weldr/api.socket http://localhost:4000/api/status | grep 'db_supported.*true'; do
            echo "#### INFO: Waiting for backend to become ready. Try $tries ..."
            tries=$((tries + 1))
            if [ $tries -gt 50 ]; then
                fail "Backend taking too long to become ready"
                # Log why starting osbuild-composer failed
                journalctl -u osbuild-composer
                exit 1
            fi
            sleep 10
        done
    else
        fail "Unable to start composer backend (exit code $RET)"
        # Log why starting osbuild-composer failed
        journalctl -u osbuild-composer
        exit $RET
    fi
}

: ${1?"Usage: $0 TOPDIR"}
TOPDIR=$1

# What versions of things do we have installed?
rpm -q weldr-client osbuild osbuild-composer

composer-cli version || fail "Getting composer-cli version"

# Start osbuild-composer
backend_start

composer-cli status show || fail "Getting osbuild-composer status"

/usr/libexec/tests/composer-cli/composer-cli-tests -test.v || fail "Running integration tests"

exit $FAILANY
