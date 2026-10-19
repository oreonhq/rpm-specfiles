%global source0_hash 6fcf18b75d305d99d04d2e42982ed5b787a081af2842220ed63287a2d6a10988
Summary:        A library for password generation and password quality checking
Name: libpwquality
Version: 1.4.5
Release:        1%{?dist}
URL: https://github.com/libpwquality/libpwquality/
Source0:        https://github.com/libpwquality/libpwquality/releases/download/libpwquality-%{version}/libpwquality-%{version}.tar.bz2
Patch1: setuptools.patch
License: BSD-3-Clause OR GPL-2.0-or-later
%global _moduledir %{_libdir}/security
%global _secconfdir %{_sysconfdir}/security
Recommends: cracklib-dicts >= 2.8
# oreon:deps
BuildRequires:  cracklib-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles python3-pwquality usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libpwquality-devel -f %{oreon_filedir}/libpwquality-devel.list
%files -n python3-pwquality -f %{oreon_filedir}/python3-pwquality.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.5-15
- Prepare for Oreon 11 (RP1)
