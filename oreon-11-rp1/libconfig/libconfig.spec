# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0ed3e37db12e38b6fd7ca85775283412043069da2edcdb0c0ddcf9160a5dcc71
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_without check

Name:                   libconfig
Summary:                C/C++ configuration file library
Version:                1.8.3
Release:                1%{?dist}
License:                LGPL-2.1-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2
URL:                    http://www.hyperrealm.com/libconfig/
Source0:                https://hyperrealm.github.io/%name/dist/%name-%version.tar.gz
Source1:                libconfig-%version.pdf

BuildRequires: oreon-rpm-macros
BuildRequires:          clang
BuildRequires:          texinfo
BuildRequires:          bison
BuildRequires:          flex
BuildRequires: make

%description
Libconfig is a simple library for manipulating structured configuration
files. This file format is more compact and more readable than XML. And
unlike XML, it is type-aware, so it is not necessary to do string parsing
in application code.

%package devel
Summary:                Development files for libconfig
Requires:               %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for developing software against
libconfig.

%prep
%oreon_sha256
%setup -q
iconv -f iso-8859-1 -t utf-8 -o AUTHORS{.utf8,}
mv AUTHORS{.utf8,}

%build
%configure \
  --disable-silent-rules \
  --disable-static

make %{?_smp_mflags}

%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
install -p %{SOURCE1} doc/

%if %{with check}
%check
make check
%endif

%ldconfig_scriptlets

%files
%license COPYING.LIB
%doc AUTHORS ChangeLog README
%{_libdir}/libconfig*.so.15*

%files devel
%doc doc/libconfig-%version.pdf
%{_includedir}/libconfig*
%{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}++
%{_libdir}/libconfig*.so
%{_libdir}/pkgconfig/libconfig*.pc
%{_infodir}/libconfig.info*

%changelog
%autochangelog
