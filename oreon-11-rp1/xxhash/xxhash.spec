%global source0_hash aae608dfe8213dfd05d909a57718ef82f30722c392344583d3f39050c7f29a80
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: xxhash
Version: 0.8.3
Release: 2%{?dist}
Summary: Extremely fast hash algorithm
License: BSD-2-Clause AND GPL-2.0-or-later
URL: https://www.xxhash.com/
Source0: https://github.com/Cyan4973/xxHash/archive/refs/tags/v%{version}.tar.gz

Requires: xxhash-libs%{?_isa} = %{version}-%{release}

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make

%description
xxHash is a fast non-cryptographic hash. This package ships xxhsum.

%package libs
Summary: xxHash library

%description libs
Shared xxHash library.

%package devel
Summary: Development files for xxHash
Requires: xxhash-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and development library for xxHash.

%prep
%oreon_sha256
%autosetup -n xxHash-%{version} -p1

%build
%ifarch x86_64
%global dispatch 1
%else
%global dispatch 0
%endif
%oreon_make MOREFLAGS="%{_oreon_cflags} %{_oreon_ldflags}" DISPATCH=%{dispatch} LIBXXH_DISPATCH=%{dispatch}

%install
%oreon_make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} DISPATCH=%{dispatch} LIBXXH_DISPATCH=%{dispatch}
rm -f %{buildroot}%{_libdir}/libxxhash.a

%ldconfig_scriptlets libs

%files
%license cli/COPYING
%{_bindir}/xxhsum
%{_bindir}/xxh32sum
%{_bindir}/xxh64sum
%{_bindir}/xxh128sum
%{_bindir}/xxh3sum
%{_mandir}/man1/xxhsum.1*
%{_mandir}/man1/xxh32sum.1*
%{_mandir}/man1/xxh64sum.1*
%{_mandir}/man1/xxh128sum.1*
%{_mandir}/man1/xxh3sum.1*

%files libs
%license LICENSE
%{_libdir}/libxxhash.so.0
%{_libdir}/libxxhash.so.0.*

%files devel
%{_includedir}/xxhash.h
%{_includedir}/xxh3.h
%if %{dispatch}
%{_includedir}/xxh_x86dispatch.h
%endif
%{_libdir}/libxxhash.so
%{_libdir}/pkgconfig/libxxhash.pc
