#!/bin/bash

if [ -s /tmp/run-job.lock ]; then
	exit 0
fi

echo $PPID > /tmp/run-job.lock
sleep 1234567
exit 0
