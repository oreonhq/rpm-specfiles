# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash eaa227686b84e8ae20181d2119c0ccac29d82371441844008019a134dafe3613
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           rpcsvc-proto
Version:        1.4
Release:        1%{?dist}
Summary:        RPC protocol definitions
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+
Url:            https://github.com/thkukuk/rpcsvc-proto
Source0:        https://github.com/thkukuk/rpcsvc-proto/archive/refs/tags/v%{version}.tar.gz#/rpcsvc-proto-%{version}.tar.gz

Conflicts: glibc-headers < 2.26.9000-36
Conflicts: glibc-common < 2.26.9000-36

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires:  clang
BuildRequires: automake
BuildRequires: autoconf

%description
The rpcsvc-proto package includes several rpcsvc header files
and RPC protocol definitions from SunRPC sources (as shipped with
glibc).

%package devel
Summary:        RPC protocol definitions

%description devel
The rpcsvc-proto package includes several rpcsvc header files
and RPC protocol definitions from SunRPC sources (as shipped with
glibc).

%package -n rpcgen
Summary:        RPC protocol compiler
Provides:       rpcgen

%description -n rpcgen
rpcgen is a tool that generates C code to implement an RPC protocol.
The input to rpcgen is a language similar to C known as RPC Language
(Remote Procedure Call Language).

%prep
%oreon_sha256
%autosetup -p 1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_prefix}/include/rpcsvc/rquota.[hx]

%files devel
%license COPYING
%{_includedir}/rpcsvc/

%files -n rpcgen
%{_bindir}/rpcgen
%{_mandir}/man1/rpcgen.1*

%changelog
%autochangelog
