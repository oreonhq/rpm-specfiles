%global source0_hash 26e1862141a3ad921b47a822243bb0896b938f9aab16f53423bee56ebf0720e8
%ifarch %{valgrind_arches}
%bcond_without csnappy_enables_valgrind
%else
%bcond_with csnappy_enables_valgrind
%endif
%global commit 6c10c305e8dde193546e6b33cf8a785d5dc123e2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:       csnappy
Version:    0
Release:        1%{?dist}
Summary:        Snappy compression library ported to C
License:    BSD-3-Clause
URL:        https://github.com/zeevt/%{name}
Source0:        https://github.com/zeevt/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:     csnappy-6c10c305e8dde193546e6b33cf8a785d5dc123e2-Fix-parallel-tests-by-only-testing-the-current-optim.patch
%if %{with csnappy_enables_valgrind}
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
This is an ANSI C port of Google's Snappy library. Snappy is a compression
library designed for speed rather than compression ratios.

%package devel
Provides:       csnappy-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:    Development files for the %{name} library
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files for developing applications that use the %{name} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{commit}

# Extract BSD license and copyright notices, bug #1152057
! test -e LICENSE
for F in $(< Makefile sed -e '/libcsnappy.so:/ s/.*:// p' -e 'd'); do
    < $F sed -e '/Copyright/,/\*\//p' -e 'd'
done > LICENSE
test -s LICENSE

%build

%{make_build} 'OPT_FLAGS=%{optflags}' 'LDFLAGS=%{?__global_ldflags}' \
    lib%{name}.so cl_tester
%check

make %{?_smp_mflags} 'OPT_FLAGS=%{optflags}' 'LDFLAGS=%{?__global_ldflags}' check_unaligned_uint64 cl_test
%if %{with csnappy_enables_valgrind}
make %{?_smp_mflags} 'OPT_FLAGS=%{optflags}' 'LDFLAGS=%{?__global_ldflags}' check_leaks
%endif
%install
%{make_install} 'DESTDIR=%{buildroot}' 'LIBDIR=%{_libdir}'
%oreon_autofiles csnappy-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n csnappy-devel -f %{oreon_filedir}/csnappy-devel.list

%changelog

%autochangelog
