#!/bin/bash
#
# Small helper script to enable EfiFs drivers using efibootmgr
# Copyright (C) 2020  Robert Scheck <robert@fedoraproject.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

[ $# -lt 1 ] && { echo "Usage: $(readlink -f "$0") </path/to/driver.efi>" >&2; exit 1; }
command -v efibootmgr &> /dev/null || { echo "Error: efibootmgr(1) is missing!" >&2; exit 1; }

for file in $@; do
  if [ -f "${file}" ]; then
    drv="$(readlink -f "${file}")"
    esp="/boot/efi"
    drv="${drv/$esp/}"
    lbl="${drv##*/}"
    lbl="${lbl%%.*}"
    efi="${drv//\//\\}"
    dev="$(findmnt -n -o source -T "${esp}")"
    part=${dev#${dev%%[0-9]*}}
    pdev="$(lsblk -dpno PKNAME "${dev}")"

    efibootmgr -r -c -d "${pdev}" -p "${part}" -L "EfiFs ${lbl}" -l "${efi}" -q
  else
    echo "$(readlink -f "${file}"): File does not exist, skipping." >&2;
  fi
done

efibootmgr -r -v
