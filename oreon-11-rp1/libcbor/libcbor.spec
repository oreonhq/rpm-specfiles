# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a8c1516e741562cf95aa4479c64916c3d4d2623e24fdc35e414e2320e7300aae

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:		libcbor
Version:        0.14.0
Release:        1%{?dist}
Summary:	A CBOR parsing library

License:	MIT
URL:		http://libcbor.org
Source0:        https://github.com/PJK/libcbor/archive/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig(cmocka)
BuildRequires:  oreon-rpm-macros
%if %{without bootstrap}
BuildRequires:	doxygen
BuildRequires:	python3-breathe
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme
%endif

%description
libcbor is a C library for parsing and generating CBOR.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{name}-devel contains development libraries and header files for %{name}.

%prep
%oreon_sha256

%autosetup


%build
%cmake -DCMAKE_BUILD_TYPE=Release -DWITH_TESTS=ON
%cmake_build
%if %{without bootstrap}
cd doc
make man
%endif

%install
%cmake_install
%if %{without bootstrap}
mkdir -p %{buildroot}%{_mandir}/man3
cp doc/build/man/libcbor.3 %{buildroot}%{_mandir}/man3/
%endif

%check
%ctest

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libcbor.so.0.14{,.*}

%files devel
%{_includedir}/cbor.h
%{_includedir}/cbor
%{_libdir}/libcbor.so
%{_libdir}/pkgconfig/libcbor.pc
%{_libdir}/cmake/libcbor
%if %{without bootstrap}
%{_mandir}/man3/libcbor.3{,.*}
%endif


%changelog
%autochangelog
