%global source0_hash ca2bb58c5e49247073a55bbf90fc804ab4d6ab7ea2711bc1e2ef793051c66f76

%define alphatag 20250303cvs

Summary: Reminder utility
Name:    calendar
Version: 1.37
Release: 14.%{alphatag}%{?dist}
License: BSD-3-Clause AND BSD-2-Clause AND ISC
URL:     http://www.openbsd.org/cgi-bin/cvsweb/src/usr.bin/calendar

# The source archive is generated with the export-calendar-source.sh
# script.  Update the script's TAG variable when a new version of
# OpenBSD is released.  The version number we use for the calendar
# program is the CVS revision ID of the calendar.c file.  This is
# determined by the script so it can make the source archive.
Source0: %{name}-%{version}-%{alphatag}.tar.gz
Source1: Makefile.linux
Source2: export-calendar-source.sh

Patch0:  %{name}-1.37-linux.patch

BuildRequires: gcc
BuildRequires: make
Requires: cpp

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

%files
%attr(755,root,root) %{_bindir}/calendar
%{_mandir}/man1/calendar.1.gz
%{_datadir}/calendar

%changelog
%autochangelog
