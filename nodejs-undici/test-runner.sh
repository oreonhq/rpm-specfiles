#!/bin/bash
set -e

# Comment out for full error trace
declare -a ignored_tests=(
    "test/http2.js"  # Some issue with custom openSSL engine in nodejs we pack. Error:0A00018F:SSL routines::ee key too small
    "test/https.js" # -/-
    "test/https2.js" # -/-
    "test/http2-dispatcher.js" # -/-
    "test/connect-pre-shared-session.js" # -/-
    "test/h2c-client.js" # -/-
    "test/connect-timeout.js" # Nodejs side issue. AssertionError [ERR_ASSERTION]: Failed
    "test/pool.js"  # @jstanek: fails in Koji, works on my laptop. ¯\_(ツ)_/¯
    "test/client-wasm.js"  # unexpected export; our clang might be too new
)

# Conditional architecture-specific ignores
ARCH=$(uname -m)

# Add architecture-specific ignores (when any)
#if [ "$ARCH" == "x86_64" ]; then
#    ignored_tests+=("test/arch-specific/x86_64/*.js")  # Example: Arch-specific test for x86_64
#elif [ "$ARCH" == "armv7l" ]; then
#    ignored_tests+=("test/arch-specific/armv7l/*.js")  # Example: Arch-specific test for armv7l
#fi

# Run borp command with the ignored tests
echo "Running tests with exclusions..."
IGNORE_ARGS=""
for test in "${ignored_tests[@]}"; do
    IGNORE_ARGS="$IGNORE_ARGS --ignore $test"
done

# Run borp with the specified ignores
exec npx borp --expose-gc -p "test/*.js" $IGNORE_ARGS
