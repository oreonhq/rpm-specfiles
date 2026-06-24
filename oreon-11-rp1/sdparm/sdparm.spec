%global source0_hash none

Summary:       List or change SCSI/SATA disk parameters
Name:          sdparm
Version:       1.12
Release:       13%{?dist}

# This software is primarily BSD-2-Clause, except for the following files:
# - BSD-2-Clause AND GPL-2.0-or-later
#     - lib/sg_pt_linux_nvme.c
# - BSD-4-Clause-UC
#     - src/getopt_long.c
#     - src/port_getopt.h
# There is also a BSD-3-Clause COPYING file, but as best I can tell no software
# files are actually covered by that license.  Headers in other files reference
# the BSD_LICENSE instead.
# Automatically converted from old format: BSD-2-Clause AND GPL-2.0-or-later AND BSD-4-Clause-UC - review is highly recommended.
License:       BSD-2-Clause AND GPL-2.0-or-later AND BSD-4-Clause-UC

URL:           http://sg.danny.cz/sg/sdparm.html
Source0:       http://sg.danny.cz/sg/p/sdparm-%{version}.tgz

# extracted from the header of lib/sg_pt_linux_nvme.c
Source1:       GPL-2.0-or-later.txt

# extracted from the header of src/getopt_long.c
Source2:       BSD-4-Clause-UC.txt

BuildRequires: make
BuildRequires: gcc
BuildRequires: sg3_utils-devel

%description 
SCSI disk parameters are held in mode pages. This utility lists or
changes those parameters. Other SCSI devices (or devices that use the
SCSI command set e.g. some SATA devices) such as CD/DVD and tape
drives may also find parts of sdparm useful.

Fetches Vital Product Data pages. Can send commands to start or stop
the media and load or unload removable media.

Warning: It is possible (but unlikely) to change SCSI disk settings
such that the disk stops operating or is slowed down. Use with care.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp %{S:1} %{S:2} .

%build
%configure --disable-libsgutils
%make_build

%install
%make_install

%files
%license BSD_LICENSE GPL-2.0-or-later.txt BSD-4-Clause-UC.txt
%doc ChangeLog README CREDITS AUTHORS notes.txt
%{_bindir}/sdparm
%{_bindir}/sas_disk_blink
%{_bindir}/scsi_ch_swp
%{_mandir}/man8/sdparm*
%{_mandir}/man8/sas_disk_blink*
%{_mandir}/man8/scsi_ch_swp*

%changelog
%autochangelog

