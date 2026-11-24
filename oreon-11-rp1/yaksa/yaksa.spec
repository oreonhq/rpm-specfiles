# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 380d5780c73b4d9623ed558daebf77f2497931783ed7403bab08682d6f25da86
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond tests 1

Name:           yaksa
Version:        0.4
Release:        %{autorelease}
Summary:        High-performance library for noncontiguous data

%global soversion 0

License:        BSD-3-Clause
URL:            https://github.com/pmodels/yaksa/
Source0:        https://github.com/pmodels/yaksa/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  uthash-devel

%description
Yaksa is a high-performance noncontiguous datatype engine that can be used to
express and manipulate noncontiguous data. The library sports features related
to packing/unpacking, I/O vectors, and flattening noncontiguous datatypes.

%package devel
Summary:        Development files for libyaksa
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
%oreon_sha256
%autosetup

ln -fvs /usr/include/uthash.h src/external/yuthash.h
ln -fvs /usr/include/utlist.h src/external/yutlist.h

%build
./autogen.sh
%configure \
    --disable-static
%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/libyaksa.la

%if %{with tests}
%check
timeout -v 2h make -j%{_smp_build_ncpus} testing
%endif

%files
%license COPYRIGHT
%doc README.md
%{_libdir}/libyaksa.so.%{soversion}{,.*}

%files devel
%{_includedir}/yaksa.h
%{_libdir}/libyaksa.so
%{_libdir}/pkgconfig/yaksa.pc

%changelog
%autochangelog
