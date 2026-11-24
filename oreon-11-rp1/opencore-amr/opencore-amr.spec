# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 483eb4061088e2b34b358e47540b5d495a96cd468e361050fae615b1809dc4a1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global sovermajor 0

Name:           opencore-amr
Version:        0.1.6
Release:        1%{?dist}
Summary:        OpenCORE Adaptive Multi Rate Narrowband and Wideband speech lib
License:        Apache-2.0
URL:            http://sourceforge.net/projects/opencore-amr/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         opencore-amr-0.1.3-fix_pc.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  make

%description
Library of OpenCORE Framework implementation of Adaptive Multi Rate Narrowband
and Wideband speech codec.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1
mv opencore/README opencore/README.opencore

%build
%configure --disable-static
%make_build

%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/libopencore-amr??.la

%ldconfig_scriptlets

%files
%doc README opencore/ChangeLog opencore/NOTICE opencore/README.opencore
%license LICENSE
%{_libdir}/libopencore-amr??.so.%{sovermajor}{,.*}

%files devel
%{_includedir}/opencore-amr??
%{_libdir}/libopencore-amr??.so
%{_libdir}/pkgconfig/opencore-amr??.pc

%changelog
%autochangelog
