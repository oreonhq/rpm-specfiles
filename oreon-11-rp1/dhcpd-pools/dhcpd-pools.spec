%global source0_hash a414e0b8061c2cba4685aff565623bcb9992699d7290a17c9f7014abe140c689

Name:		dhcpd-pools
Version:	3.3
Release:	4%{?dist}
Summary:	ISC dhcpd lease analysis and reporting
# BSD: dhcpd-pools
# ASL 2.0: mustache templating (https://gitlab.com/jobol/mustach) src/mustach.[ch]
# GPLv3+: gnulib (https://www.gnu.org/software/gnulib/) lib/
License:	BSD-2-Clause AND Apache-2.0 AND GPL-3.0-or-later
URL:		https://dhcpd-pools.sourceforge.net/
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0:		dhcpd-pools-test-color.patch
Patch1:		0001-f44_hack.patch
BuildRequires:	uthash-devel
BuildRequires:	gcc, make
BuildRequires:	perl-generators
Provides:	bundled(gnulib) = 2025

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
%if 0%{?fedora} >= 44
%patch -P1 -p1
%endif

%build
# configure to match OS install defaults
%configure \
    --with-dhcpd-conf=%{_sysconfdir}/dhcp/dhcpd.conf \
    --with-dhcpd-leases=%{_localstatedir}/lib/dhcpd/dhcpd.leases

make %{?_smp_mflags}

%install
%make_install
# make install installs docs, let rpmbuild handle it
rm -rf %{buildroot}%{_docdir}/%{name}

# original encoding appears to be ISO8859-1
iconv --from=ISO8859-1 --to=UTF-8 THANKS > THANKS.utf8
touch --reference=THANKS THANKS.utf8
mv THANKS.utf8 THANKS

# add munin plugin but not executable
chmod -x contrib/munin_plugins/*

%check
make check-TESTS

%files
%license COPYING
%doc README THANKS TODO AUTHORS ChangeLog
%doc samples/*.template
%doc contrib/munin_plugins
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/%{name}/

%changelog
%autochangelog
