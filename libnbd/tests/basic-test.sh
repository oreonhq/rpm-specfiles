#!/bin/bash -
set -e
set -x

# Enable libnbd debugging.
export LIBNBD_DEBUG=1

# Connect to nbdkit.
nbdsh -c - <<EOF
h.connect_command (["nbdkit", "-s", "--exit-with-parent",
                    "memory", "size=1G"])
size = h.get_size ()
print ("size = %s" % size)
assert size == 1073741824
EOF
