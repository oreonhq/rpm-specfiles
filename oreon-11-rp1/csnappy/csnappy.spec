%global source0_hash 26e1862141a3ad921b47a822243bb0896b938f9aab16f53423bee56ebf0720e8

# Run valgrind test
# valgrind is available only on selected arches
%ifarch %{valgrind_arches}
%bcond_without csnappy_enables_valgrind
%else
%bcond_with csnappy_enables_valgrind
%endif

%global commit 6c10c305e8dde193546e6b33cf8a785d5dc123e2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       csnappy
Version:    0
Release:    34.20211216git%{shortcommit}%{?dist}
Summary:    Snappy compression library ported to C 
License:    BSD-3-Clause
URL:        https://github.com/zeevt/%{name}
Source0:    %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
# Fix parallel tests, <https://github.com/zeevt/csnappy/pull/40>
Patch0:     csnappy-6c10c305e8dde193546e6b33cf8a785d5dc123e2-Fix-parallel-tests-by-only-testing-the-current-optim.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# Tests:
BuildRequires:  coreutils
BuildRequires:  diffutils
BuildRequires:  gzip
%if %{with csnappy_enables_valgrind}
BuildRequires:  valgrind
%endif

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

%files
%license LICENSE
%doc README TODO
# No soname <https://github.com/zeevt/csnappy/issues/33>
%{_libdir}/lib%{name}.so

%files devel
%{_includedir}/%{name}.h


%changelog
%autochangelog
