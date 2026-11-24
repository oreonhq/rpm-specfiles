# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 90f8d2fa8b5567c6899830ddef2c03f3c27960b11aca222fa17aa7ac613c2890
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           duktape
Version:        2.7.0
Release:        1%{?dist}
Summary:        Embeddable Javascript engine

License:        MIT
Url:            http://duktape.org/
Source0:        https://duktape.org/%{name}-%{version}.tar.xz
Patch0:        duktape-2.7.0-link-against-libm.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  pkgconfig
BuildRequires:  make

%description
Duktape is an embeddable Javascript engine, with a focus on portability and
compact footprint.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
Embeddable Javascript engine.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%make_build -f Makefile.sharedlibrary INSTALL_PREFIX=%{_prefix} LIBDIR=/%{_lib}

%install
%make_install -f Makefile.sharedlibrary INSTALL_PREFIX=%{_prefix} LIBDIR=/%{_lib}

%files
%license LICENSE.txt
%doc AUTHORS.rst
%{_libdir}/libduktape.so.*
%{_libdir}/libduktaped.so.*

%files devel
%doc examples/ README.rst
%{_includedir}/duk_config.h
%{_includedir}/duktape.h
%{_libdir}/libduktape.so
%{_libdir}/libduktaped.so
%{_libdir}/pkgconfig/duktape.pc

%changelog
%autochangelog
