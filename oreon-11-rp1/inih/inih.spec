# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5d7967de62c5bfdc4f9f5ab06ce44c9e498bae021c7dac5792c0696e76aa9963
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:     inih
Version:  63
Release:  1%{?dist}
Summary:  Simple INI file parser library

License:  BSD-3-Clause
URL:      https://github.com/benhoyt/inih
Source0:  %{url}/archive/r%{version}/%{name}-r%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: meson


%description
The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.

%package cpp
Summary: INIReader C++ library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description cpp
This package contains the INIReader C++ library which provides a C++ interface
for inih.

%package devel
Summary:  Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-cpp%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.



%prep
%oreon_sha256
%autosetup -n %{name}-r%{version}

%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/lib%{name}.so.0

%files cpp
%{_libdir}/libINIReader.so.0

%files devel
%{_includedir}/ini.h
%{_includedir}/INIReader.h
%{_libdir}/pkgconfig/inih.pc
%{_libdir}/pkgconfig/INIReader.pc
%{_libdir}/lib%{name}.so
%{_libdir}/libINIReader.so


%changelog
%autochangelog
