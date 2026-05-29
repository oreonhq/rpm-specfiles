%global source0_hash 6fcf18b75d305d99d04d2e42982ed5b787a081af2842220ed63287a2d6a10988

Summary: A library for password generation and password quality checking
Name: libpwquality
Version: 1.4.5
Release: 15%{?dist}
URL: https://github.com/libpwquality/libpwquality/
Source0:        https://github.com/libpwquality/libpwquality/releases/download/libpwquality-1.4.5/libpwquality-1.4.5.tar.bz2

# Use setuptools instead of distutils
# This fixes the build with Python 3.12+
# https://bugzilla.redhat.com/2165572
# Upstream PR: https://github.com/libpwquality/libpwquality/pull/74
Patch1: setuptools.patch

# The package is BSD licensed with option to relicense as GPLv2+
# - this option is redundant as the BSD license allows that anyway.
License: BSD-3-Clause OR GPL-2.0-or-later

%global _moduledir %{_libdir}/security
%global _secconfdir %{_sysconfdir}/security

# This allows minimal installs to not drag in the big wordlist package
# but anyone doing this should be careful as it causes various
# password set/change operations to fail
Recommends: cracklib-dicts >= 2.8

BuildRequires: gcc make
BuildRequires: cracklib-devel
BuildRequires: gettext
BuildRequires: pam-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This is a library for password quality checks and generation
of random passwords that pass the checks.
This library uses the cracklib and cracklib dictionaries
to perform some of the checks.

%package devel
Summary: Support for development of applications using the libpwquality library
Requires: libpwquality%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Files needed for development of applications using the libpwquality
library.
See the pwquality.h header file for the API.

%package -n python3-pwquality
Summary: Python bindings for the libpwquality library
Requires: libpwquality%{?_isa} = %{version}-%{release}

%description -n python3-pwquality
This is pwquality Python module that provides Python bindings
for the libpwquality library. These bindings can be used
for easy password quality checking and generation of random
pronounceable passwords from Python applications.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%configure \
	--with-securedir=%{_moduledir} \
	--with-pythonsitedir=%{python3_sitearch} \
	--with-python-binary=%{__python3} \
	--disable-static

%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_moduledir}/*.la
mkdir %{buildroot}%{_secconfdir}/pwquality.conf.d

%find_lang libpwquality

%check
# Nothing yet

%ldconfig_scriptlets

%files -f libpwquality.lang
%license COPYING
%doc README NEWS AUTHORS
%{_bindir}/pwmake
%{_bindir}/pwscore
%dir %{_moduledir}
%{_moduledir}/pam_pwquality.so
%{_libdir}/libpwquality.so.*
%dir %{_secconfdir}
%config(noreplace) %{_secconfdir}/pwquality.conf
%dir %{_secconfdir}/pwquality.conf.d
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%{_includedir}/pwquality.h
%{_libdir}/libpwquality.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%files -n python3-pwquality
%{python3_sitearch}/*.so
%{python3_sitearch}/*.egg-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.5-15
- Prepare for Oreon 11 (RP1)
