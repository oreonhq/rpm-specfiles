%global source0_hash a414e0b8061c2cba4685aff565623bcb9992699d7290a17c9f7014abe140c689
Name:		dhcpd-pools
Version:	3.3
Release:        4%{?dist}
Summary:        ISC dhcpd lease analysis and reporting
License:	BSD-2-Clause AND Apache-2.0 AND GPL-3.0-or-later
URL:		https://dhcpd-pools.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0:		dhcpd-pools-test-color.patch
Patch1:		0001-f44_hack.patch
Provides:	bundled(gnulib) = 2025
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  uthash-devel
# /oreon:deps
%description
This is for ISC DHCP shared network and pool range usage analysis.  Purpose
of command is to count usage ratio of each IP range and shared network pool
which ISC dhcpd is in control of. Users of the command are most likely ISPs
and other organizations that have large IP space.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# "errors" test output has ANSI color, strip/disable
%patch -P0 -p1

%build

%configure \
    --with-dhcpd-conf=%{_sysconfdir}/dhcp/dhcpd.conf \
    --with-dhcpd-leases=%{_localstatedir}/lib/dhcpd/dhcpd.leases
make %{?_smp_mflags}
%install
%make_install
rm -rf %{buildroot}%{_docdir}/%{name}
iconv --from=ISO8859-1 --to=UTF-8 THANKS > THANKS.utf8
touch --reference=THANKS THANKS.utf8
mv THANKS.utf8 THANKS
chmod -x contrib/munin_plugins/*
%oreon_autofiles main

%check

make check-TESTS
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
