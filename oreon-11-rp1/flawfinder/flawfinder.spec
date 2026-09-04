%global source0_hash 9d732a4e0fef1cd4eaeefd4a0093f183c5981f6c843711ceae6a63419404996b

Summary: Examines C/C++ source code for security flaws
Name: flawfinder
Version: 2.0.20
Release: 1%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL: http://www.dwheeler.com/flawfinder/

BuildArch: noarch
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Flawfinder scans through C/C++ source code,
identifying lines ("hits") with potential security flaws.
By default it reports hits sorted by severity, with the riskiest lines first.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup  -q
# Substitute the shebang to use python3
sed -i '1s@^#!/usr/bin/env python@#!/usr/bin/python3@' flawfinder

%build
make

%install
install -p -m755 -D flawfinder %{buildroot}%{_bindir}/flawfinder
install -p -m644 -D flawfinder.1 %{buildroot}%{_mandir}/man1/flawfinder.1

%files
%doc README.md ChangeLog
%license COPYING
%{_bindir}/flawfinder
%{_mandir}/man1/flawfinder.1*

%changelog
%autochangelog
