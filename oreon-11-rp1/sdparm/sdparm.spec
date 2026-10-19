%global source0_hash e7f84247069da9a0c293963948d8aba8e5897a13e35e5476c8258acb7ca3a124
Summary:        List or change SCSI/SATA disk parameters
Name:          sdparm
Version:       1.12
Release:        13%{?dist}
License:       BSD-2-Clause AND GPL-2.0-or-later AND BSD-4-Clause-UC
URL:           http://sg.danny.cz/sg/sdparm.html
Source0:        http://sg.danny.cz/sg/p/sdparm-%{version}.tgz
Source1:       GPL-2.0-or-later.txt
Source2:       BSD-4-Clause-UC.txt
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sg3_utils-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

