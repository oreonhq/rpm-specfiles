# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b88cc9163d0c652aaf39a99991d974ddba1c3a9711db8f1b5838af2a14731014
%global source1_hash 620dc92f158ebe0a650c0e92214a8121b927276895dc9a1dcaa38f627fa0fcb0
%global source2_hash 56b3e6dc62d6de533d1a86621b3d3fe8f9523a83f2b19927a95cffb8b562150b
%global source3_hash 5f85ce9374352a2ad21ab2bbc42a4a95ea4a05da010bf128ece0d0327dc54605
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libbsd
Version:        0.12.2
Release:        1%{?dist}
Summary:        Library providing BSD-compatible functions for portability
URL:            https://libbsd.freedesktop.org/
License:        Beerware AND BSD-2-Clause AND BSD-3-Clause AND ISC AND libutil-David-Nugent AND MIT AND LicenseRef-Fedora-Public-Domain

Source0:        https://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz
Source1:        https://libbsd.freedesktop.org/releases/libbsd-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/4F3E74F436050C10F5696574B972BF3EA4AE57A3
Source3:        libbsd-cdefs.h

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
%if 0%{?fedora} || 0%{?rhel} >= 9 || 0%{?oreon}
BuildRequires:  openpgpverify
%else
BuildRequires:  gnupg2
%endif
BuildRequires:  libmd-devel
BuildRequires:  make

%description
libbsd provides useful functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port
projects with strong BSD origins, without needing to embed the same
code over and over again on each project.

%package devel
Summary:        Development files for libbsd
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libmd-devel

%description devel
Development files for the libbsd library.

%package ctor-static
Summary:        Development files for libbsd
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description ctor-static
The libbsd-ctor static library is required if setproctitle() is to be used
when libbsd is loaded via dlopen() from a threaded program.  This can be
configured using "pkg-config --libs libbsd-ctor".

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
%setup -q
%{?openpgpverify}%{!?openpgpverify:%{gpgverify}} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%build
%configure
%make_build

%check
%make_build check

%install
%make_install

rm %{buildroot}%{_libdir}/%{name}.a
rm %{buildroot}%{_libdir}/%{name}.la

mv -f %{buildroot}%{_includedir}/bsd/sys/cdefs{,-%{__isa_bits}}.h
install -p -m 0644 %{SOURCE3} %{buildroot}%{_includedir}/bsd/sys/cdefs.h

%ldconfig_scriptlets

%files
%license COPYING
%doc README ChangeLog
%{_libdir}/%{name}.so.0*

%files devel
%{_mandir}/man3/*.3bsd.*
%{_mandir}/man7/%{name}.7.*
%{_includedir}/bsd
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-overlay.pc

%files ctor-static
%{_libdir}/%{name}-ctor.a
%{_libdir}/pkgconfig/%{name}-ctor.pc

%changelog
%autochangelog
