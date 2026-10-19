%global source0_hash ca2bb58c5e49247073a55bbf90fc804ab4d6ab7ea2711bc1e2ef793051c66f76
%define alphatag 20250303cvs
Summary:        Reminder utility
Name:    calendar
Version: 1.37
Release:        1%{?dist}
License: BSD-3-Clause AND BSD-2-Clause AND ISC
URL:     http://www.openbsd.org/cgi-bin/cvsweb/src/usr.bin/calendar
Source0:        %{name}-%{version}-%{alphatag}.tar.gz
Source1: Makefile.linux
Source2: export-calendar-source.sh
Patch0:  %{name}-1.37-linux.patch
Requires: cpp
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The OpenBSD calendar command is a reminder utility.  Calendar reads
a mix of configuration files and standard calendar databases and
then displays lines that begin with either today's date or
tomorrow's.  The output of the command shows upcoming events for the
week.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-%{alphatag}
cp %{SOURCE1} Makefile

for c in calendars/*.*/* ; do
    fromcode="$(grep '^LANG=' "$c" | sed 's/^LANG=\(.*\)\.\(.*\)\(@.*\)\{0,1\}/\2/')"
    if [ ! -z "$fromcode" ]; then
        iconv -f "$fromcode" -t "UTF-8" "$c" > "$c.conv"
        mv "$c.conv" "$c"
    fi
done

%build

%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
