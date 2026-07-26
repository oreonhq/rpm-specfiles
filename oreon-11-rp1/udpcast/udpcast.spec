%global source0_hash a3cebee7a87ecf1bca0645f125be78fbd7b37846a4da82fecef96b92cc64d050

Name:          udpcast
Summary:       UDP broadcast file distribution and installation
Version:       20211207
Release:       13%{?dist}
License:       GPL-2.0-or-later AND BSD-2-Clause-first-lines AND MPL-1.1
URL:           http://udpcast.linux.lu/
Source:        https://www.udpcast.linux.lu/download/%{name}-%{version}.tar.gz

# Fix console.c:89:7: warning: ignoring return value of 'read'
Patch1:        udpcast-20200328-read-warn.patch

# Fix hardcoded sbin dir
Patch2:        udpcast-20211207-makefile-in.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: m4
BuildRequires: perl-interpreter
BuildRequires: /usr/bin/pod2man

%description
Command-line client for UDP sender and receiver.  Udpcast is an
application for multicasting data to multiple targets.

%package devel
Summary:        Development headers for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
Command-line client for UDP sender and receiver.  Udpcast is an
application for multicasting data to multiple targets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc Changelog.txt cmd.html COPYING
%{_sbindir}/udp-sender
%{_sbindir}/udp-receiver
%{_mandir}/man1/udp-sender.1*
%{_mandir}/man1/udp-receiver.1*

%files devel
%doc COPYING
%{_includedir}/udpcast/rateGovernor.h

%changelog
%autochangelog
