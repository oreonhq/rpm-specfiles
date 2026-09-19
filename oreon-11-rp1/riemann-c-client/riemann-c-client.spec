%global source0_hash 568416d854d1c1e5eac743c9f56db6fa0d6a8144daa74a799d0556bb6b50e679

#
# spec file for package riemann-c-client
#
# Copyright (c) 2014 Peter Czanik, Budapest, Hungary.
#

%global sover 0

Name:		riemann-c-client
Version:	1.10.5
Release:	14%{?dist}
Summary:	The riemann C client
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
Url:		https://github.com/algernon/riemann-c-client
Source0:	%{url}/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0000:	riemann-c-client-1.10.5-gcc10_symver.patch
Patch0001:      fix-gnutls-send-recv-when-return-eagain
Patch0002:      fix-gnutls-send-recv-when-return-less-than-expected
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig
BuildRequires:	protobuf-c-devel
BuildRequires:	json-c-devel
BuildRequires:  gnutls-devel

%description
This is a C client library for the Riemann monitoring system, providing a
convenient and simple API, high test coverage and a copyleft license,
along with API and ABI stability.

%package devel
Summary:	Development files for riemann-c-client
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	protobuf-c-devel%{?_isa}
Requires:	json-c-devel

%description devel
This package provides files necessary for riemann-c-client development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{name}-%{version}
%patch -P0 -p1 -b.gcc10_symver
%patch -P1 -p1
%patch -P2 -p1
autoreconf -fiv

%build
%configure --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/libriemann-client.la

%ldconfig_scriptlets

%files
%doc README.md NEWS.md
%license LICENSE*
%{_libdir}/libriemann-client.so.%{sover}*
%{_bindir}/riemann-client
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/riemann/
%{_libdir}/libriemann-client.so
%{_libdir}/pkgconfig/riemann-client.pc

%changelog
%autochangelog
