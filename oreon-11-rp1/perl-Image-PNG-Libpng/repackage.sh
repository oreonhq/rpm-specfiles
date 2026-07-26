#!/bin/bash
#
# Copyright (C) 2010, 2021 Red Hat, Inc.
# Authors:
# Thomas Woerner <twoerner@redhat.com>
# Petr Pisar <ppisar@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

version=$1
[ -z "$version" ] && { echo "Usage: $0 <version>"; exit 1; }

# files to be removed without the main SDL-<version>/ prefix
declare -a REMOVE
REMOVE[${#REMOVE[*]}]="examples/life.png"
REMOVE[${#REMOVE[*]}]="examples/life-gray.png"
REMOVE[${#REMOVE[*]}]="t/tantei-san.png"

# no changes below this line should be needed

orig="Image-PNG-Libpng-${version}"
orig_tgz="${orig}.tar.gz"
repackaged="${orig}_repackaged"
repackaged_tar="${repackaged}.tar"
repackaged_tgz="${repackaged_tar}.gz"

# pre checks
[ ! -f "${orig_tgz}" ] && { echo "ERROR: ${orig_tgz} does not exist"; exit 1; }
[ -d "${orig}" ] && { echo "ERROR: ${orig} directory already exist"; exit 1; }
[ -f "${repackaged_tgz}" ] && { echo "ERROR: ${repackaged_tgz} already exist"; exit 1; }

# repackage
failure=0
tar -xzf "${orig_tgz}"
for file in "${REMOVE[@]}"; do
    rm "${orig}/${file}" 2>> repackage.log
    [ $? != 0 ] && { echo "ERROR: Could not remove ${orig}/${file} file."; failure=1; } || echo "${orig}/${file} removed."
done
[ $failure != 0 ] && { echo "See repackage.log for the details."; exit 1; }
tar -czf "${repackaged_tgz}" "${orig}"

# post checks
RET=0
for file in "${REMOVE[@]}"; do
    found=$(tar -ztvf "${repackaged_tgz}" | grep "${file}")
    [ -n "$found" ] && { echo "ERROR: file ${file} is still in the repackaged archive."; RET=1; }
done

[ $RET == 0 ] && echo "Sucessfully repackaged ${orig}: ${repackaged_tgz}"

exit $RET
