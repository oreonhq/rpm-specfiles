%global source0_hash df66150429a59a3b6cea9b29e2687707d04ab10db5dfe1c893ba3e0b0531b151

Name:		dhtest
Version:	1.5
Release:	19%{?snapinfo:.%{snapinfo}}%{?dist}
Summary:	A DHCP client simulation on linux

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://github.com/saravana815/dhtest
Source0:	https://github.com/saravana815/dhtest/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		dhtest-1.5-globals.patch
Patch2:		dhtest-1.5-strncpy.patch

BuildRequires:	gcc
BuildRequires: make

%description
It can simulate multiple DHCP clients behind a network device.
It can help in testing the DHCP servers or in testing switch/router
by loading the device with multiple DHCP clients.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
#sed -e 's,^#!/usr/bin/env python,#!/usr/bin/python,' -i dhscript.py

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
mkdir -p %{buildroot}%{_bindir}
%{__install} -m 0755 dhtest %{buildroot}%{_bindir}/dhtest

%check
# run dhscript.py here once it can run without special setup
# or dhcp server is configured

%files
%doc README.txt
%license LICENSE
%{_bindir}/dhtest

%changelog
%autochangelog
