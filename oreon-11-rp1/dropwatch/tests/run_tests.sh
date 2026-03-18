#!/bin/bash

abort_dropwatch() {
	sleep 5
	killall -SIGINT dropwatch
}

abort_dropwatch &
echo -e "set alertlimit 1\nstart\nstop\nexit" | dropwatch -l kas &> "$TMT_TEST_DATA"/dropwatch.log

# shellcheck disable=SC2181
[ $? -eq 0 ] && exit 0
# If the platform doesn't support NET_DM, skip this test
# Usually we got this issue in container as no privilege permission
grep -q NET_DM "$TMT_TEST_DATA"/dropwatch.log && exit 0 || exit 1
