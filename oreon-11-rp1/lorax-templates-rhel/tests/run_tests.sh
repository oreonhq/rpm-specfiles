#!/bin/bash
set -eux

if [ ! -e /usr/share/lorax/templates.d/80-rhel/ ]; then
    echo "Failed to find lorax-templates-rhel templates in /usr/share/lorax/templates.d/"
    exit 1
fi

# Gather up the list of system repo files and use them for lorax
# Skip fedora.repo
REPOS=$(find /etc/yum.repos.d/ -maxdepth 1 -type f -name '*\.repo' ! -name 'fedora.repo' -exec echo -n "--repo {} " \;)
if [ -z "$REPOS" ]; then
    echo "No system repos found"
    exit 1
fi

# Run lorax using the host's repository configuration file
lorax --product="Red Hat Enterprise Linux" --version=11 --release=11 --volid="RHEL-11-test" \
      $REPOS --isfinal --nomacboot /var/tmp/lorax-rhel11-iso/
