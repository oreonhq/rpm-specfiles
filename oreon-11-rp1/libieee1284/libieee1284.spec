# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7730de107782e5d2b071bdcb5b06a44da74856f00ef4a9be85d1ba4806a38f1a
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary: A library for interfacing IEEE 1284-compatible devices
Name: libieee1284
Version: 0.2.11
Release: 48%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://cyberelk.net/tim/libieee1284/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch1: libieee1284-strict-aliasing.patch
BuildRequires: gcc
BuildRequires: xmlto
BuildRequires: make
BuildRequires: libtool

%description
The libieee1284 library is for communicating with parallel port devices.

%package devel
Summary: Files for developing applications that use libieee1284
Requires: %{name} = %{version}-%{release}

%description devel
The header files, static library, libtool library and man pages for
developing applications that use libieee1284.

%prep
%oreon_verify_sources
%setup -q
# Fixed strict aliasing warnings (bug #605170).
%patch -P1 -p1 -b .strict-aliasing

%build
autoreconf -iv
touch doc/interface.xml
%configure --without-python
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -f %{buildroot}%{_libdir}/python*/*/*a
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%files
%doc README COPYING TODO AUTHORS NEWS
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%{_includedir}/ieee1284.h
%{_libdir}/*.so
%{_mandir}/*/*

%ldconfig_scriptlets

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.11-48
- Prepare for Oreon 11 (RP1)
