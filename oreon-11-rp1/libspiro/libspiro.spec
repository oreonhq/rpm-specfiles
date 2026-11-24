# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1412a21b943c6e1db834ee2d74145aad20b3f62b12152d475613b8241d9cde10
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libspiro
Version:        20240903
Release:        1%{?dist}
Summary:        Library to simplify the drawing of beautiful curves

License:        GPL-3.0-or-later
URL:            https://github.com/fontforge/libspiro/
Source0:        https://github.com/fontforge/libspiro/releases/download/%{version}/libspiro-dist-%{version}.tar.gz
BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires: make

%description
This library will take an array of spiro control points and 
convert them into a series of bézier splines which can then 
be used in the myriad of ways the world has come to use béziers. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -n libspiro-%{version}

%build
%configure --disable-static
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
make check

%files
%doc README* ChangeLog AUTHORS
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libspiro.pc
%{_mandir}/man3/libspiro.3.gz

%changelog
%autochangelog
