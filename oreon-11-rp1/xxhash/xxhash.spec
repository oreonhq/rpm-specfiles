%global source0_hash 5738270935e7c3d38a79b3adf7c9692566ce7895a25f67de43ad52ab504acd32
Name:		xxhash
Version:	0.8.4
Release:        1%{?dist}
Summary:        Extremely fast hash algorithm
License:	BSD-2-Clause AND GPL-2.0-or-later
URL:		https://www.xxhash.com/
Source0:        https://github.com/Cyan4973/xxHash/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n xxHash-%{version}

%build

%ifarch %{ix86} x86_64
%global dispatch 1
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
    DISPATCH=%{dispatch} \
    LIBXXH_DISPATCH=%{dispatch}
rm %{buildroot}/%{_libdir}/libxxhash.a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
make test-xxhsum-c
%files -f %{oreon_filedir}/main.list
%files -n xxhash-libs -f %{oreon_filedir}/xxhash-libs.list
%files -n xxhash-devel -f %{oreon_filedir}/xxhash-devel.list
%files -n xxhash-doc -f %{oreon_filedir}/xxhash-doc.list

%changelog

%autochangelog
