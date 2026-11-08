# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5738270935e7c3d38a79b3adf7c9692566ce7895a25f67de43ad52ab504acd32

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:		xxhash
Version:        0.8.4
Release:        1%{?dist}
Summary:	Extremely fast hash algorithm

#		The source for the library (xxhash.c and xxhash.h) is BSD-2-Clause
#		The source for the command line tool (xxhsum.c) is GPL-2.0-or-later
License:	BSD-2-Clause AND GPL-2.0-or-later
URL:		https://www.xxhash.com/
Source0:        https://github.com/Cyan4973/xxHash/archive/v%{version}/xxhash-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	doxygen
BuildRequires:  oreon-rpm-macros

%description
xxHash is an Extremely fast Hash algorithm, running at RAM speed
limits. It successfully completes the SMHasher test suite which
evaluates collision, dispersion and randomness qualities of hash
functions. Code is highly portable, and hashes are identical on all
platforms (little / big endian).

%package libs
Summary:	Extremely fast hash algorithm - library
License:	BSD-2-Clause

%description libs
xxHash is an Extremely fast Hash algorithm, running at RAM speed
limits. It successfully completes the SMHasher test suite which
evaluates collision, dispersion and randomness qualities of hash
functions. Code is highly portable, and hashes are identical on all
platforms (little / big endian).

%package devel
Summary:	Extremely fast hash algorithm - development files
License:	BSD-2-Clause
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
# By setting XXH_INLINE_ALL, xxhash may be used as a header-only library.
# Dependent packages that use xxhash this way must BR this virtual Provide:
Provides:	%{name}-static = %{version}-%{release}

%description devel
Development files for the xxhash library

%package doc
Summary:	Extremely fast hash algorithm - documentation files
License:	BSD-2-Clause
BuildArch:	noarch

%description doc
Documentation files for the xxhash library

%prep
%oreon_sha256

%setup -q -n xxHash-%{version}

%build
# Enable runtime detection of sse2/avx2/avx512 on intel architectures
%ifarch %{ix86} x86_64
%global dispatch 1
# Some distribution variants build with -march=x86-64-v3.
# See xxh_x86dispatch.c.
%global moreflags_dispatch -DXXH_X86DISPATCH_ALLOW_AVX
%else
%global dispatch 0
%global moreflags_dispatch %{nil}
%endif

%make_build \
    MOREFLAGS="%{__global_cflags} %{?__global_ldflags} %{moreflags_dispatch}" \
    DISPATCH=%{dispatch} \
    LIBXXH_DISPATCH=%{dispatch}
doxygen

%install
%make_install \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    MOREFLAGS="%{__global_cflags} %{?__global_ldflags} %{moreflags_dispatch}" \
    DISPATCH=%{dispatch} \
    LIBXXH_DISPATCH=%{dispatch}
rm %{buildroot}/%{_libdir}/libxxhash.a

%check
make check \
    MOREFLAGS="%{__global_cflags} %{?__global_ldflags} %{moreflags_dispatch}" \
    DISPATCH=%{dispatch} \
    LIBXXH_DISPATCH=%{dispatch}
make test-xxhsum-c \
    MOREFLAGS="%{__global_cflags} %{?__global_ldflags} %{moreflags_dispatch}" \
    DISPATCH=%{dispatch} \
    LIBXXH_DISPATCH=%{dispatch}

%files
%{_bindir}/xxh*sum
%{_mandir}/man1/xxh*sum.1*
%license cli/COPYING
%doc cli/README.md

%files libs
%{_libdir}/libxxhash.so.*
%license LICENSE
%doc README.md

%files devel
%{_includedir}/xxhash.h
%{_includedir}/xxh3.h
%if %{?dispatch}
%{_includedir}/xxh_x86dispatch.h
%endif
%{_libdir}/libxxhash.so
%{_libdir}/pkgconfig/libxxhash.pc

%files doc
%doc doxygen/html

