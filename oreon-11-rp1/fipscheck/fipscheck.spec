# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 024953c8bee1458aa9c48dc0648420c503ed71c37ce6b366ce296fad2f217889

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: fipscheck
Version: 1.7.0
Release: 1%{?dist}
Summary: Library for integrity verification of FIPS modules
License: BSD-2-Clause
URL: https://github.com/Ezurio/fipscheck
Source0: https://api.opensuse.org/public/source/openSUSE:Factory/fipscheck/fipscheck-%{version}.tar.bz2
Patch0: fipscheck-fix_check_openssl_version.patch
Patch1: fipscheck-fix_incorrect_length_type.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pkgconfig(openssl)

Requires: %{name}-lib%{?_isa} = %{version}-%{release}

%description
FIPSCheck is a library for integrity verification of FIPS validated
modules. The package also provides helper binaries for creation and
verification of the HMAC-SHA256 checksum files.

%package lib
Summary: Library files for %{name}
Requires: %{_bindir}/fipscheck

%description lib
This package contains the FIPSCheck library.

%package devel
Summary: Development files for %{name}
Requires: %{name}-lib%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --disable-static
%make_build

%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    mkdir -p %{buildroot}%{_libdir}/fipscheck \
    %{buildroot}%{_bindir}/fipshmac -d %{buildroot}%{_libdir}/fipscheck \
        %{buildroot}%{_bindir}/fipscheck \
        %{buildroot}%{_libdir}/libfipscheck.so.1.2.1 \
    ln -sf libfipscheck.so.1.2.1.hmac \
        %{buildroot}%{_libdir}/fipscheck/libfipscheck.so.1.hmac \
%{nil}

%install
%make_install
find %{buildroot} -type f -name '*.la' -delete
mkdir -p %{buildroot}%{_libdir}/fipscheck

%check
%make_build check

%ldconfig_scriptlets lib

%files
%license COPYING
%doc ChangeLog README NEWS AUTHORS
%{_bindir}/fipscheck
%{_bindir}/fipshmac
%{_libdir}/fipscheck/fipscheck.hmac
%{_mandir}/man8/*

%files lib
%{_libdir}/libfipscheck.so.*
%dir %{_libdir}/fipscheck
%{_libdir}/fipscheck/libfipscheck.so.*.hmac

%files devel
%{_includedir}/fipscheck.h
%{_libdir}/libfipscheck.so
%{_mandir}/man3/*

%changelog
%autochangelog
