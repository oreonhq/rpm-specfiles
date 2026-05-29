%global source0_hash aae608dfe8213dfd05d909a57718ef82f30722c392344583d3f39050c7f29a80

Name:		xxhash
Version:	0.8.3
Release:	4%{?dist}
Summary:	Extremely fast hash algorithm

#		The source for the library (xxhash.c and xxhash.h) is BSD-2-Clause
#		The source for the command line tool (xxhsum.c) is GPL-2.0-or-later
License:	BSD-2-Clause AND GPL-2.0-or-later
URL:		https://www.xxhash.com/
Source0:        https://github.com/Cyan4973/xxHash/archive/v0.8.3/xxhash-0.8.3.tar.gz

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	doxygen

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
    DISPATCH=%{dispatch} \
    LIBXXH_DISPATCH=%{dispatch}
rm %{buildroot}/%{_libdir}/libxxhash.a

%check
make check
make test-xxhsum-c

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

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.3-4
- Prepare for Oreon 11 (RP1)
