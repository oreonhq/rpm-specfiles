# Uncomment on initial build for soname bump.
#global bump_soname 1
%global sover 3

%if 0%{?bump_soname}
%global relsuffix ~sonamebump
%global old_sover %(echo $((%{sover}-1)))
%endif

Name:       libnsl2
Version:    2.0.1
Release:    5%{?relsuffix}%{?dist}
Summary:    Public client interface library for NIS(YP) and NIS+

License:    BSD-3-Clause AND LGPL-2.1-or-later
URL:        https://github.com/thkukuk/libnsl

Source0:    https://github.com/thkukuk/libnsl/archive/v%{version}.tar.gz

BuildRequires: autoconf, automake, gettext-devel, libtool, libtirpc-devel
BuildRequires: make
BuildRequires: gcc
%if 0%{?bump_soname}
BuildRequires: libnsl2 < %{version}
%endif

%description
This package contains the libnsl library. This library contains
the public client interface for NIS(YP) and NIS+.
This code was formerly part of glibc, but is now standalone to
be able to link against TI-RPC for IPv6 support.

%package devel
Summary: Development files for libnsl
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: glibc-devel < 2.26.9000-40

%description devel
Development files for libnsl2


%prep
%setup -q -n libnsl-%{version}

%build
autoreconf -fiv

%configure \
    --libdir=%{_libdir} \
    --includedir=%{_includedir}

%make_build


%install
%make_install

rm %{buildroot}%{_libdir}/libnsl.{a,la}

%if 0%{?bump_soname}
cp -p %{_libdir}/libnsl.so.%{old_sover}* %{buildroot}%{_libdir}
%endif

%files
%license COPYING
%{_libdir}/libnsl.so.%{sover}*
%if 0%{?bump_soname}
%{_libdir}/libnsl.so.%{old_sover}*
%endif

%files devel
%{_libdir}/libnsl.so
%{_includedir}/*
%{_libdir}/pkgconfig/libnsl.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-5
- Prepare for Oreon 11 (RP1)
