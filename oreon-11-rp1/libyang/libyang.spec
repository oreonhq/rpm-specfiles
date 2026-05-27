%global source0_hash none

%global run_valgrind_tests ON
# valgrind finds invalid writes in libcmocka on arm and power
# see bug #1699304 for more information
%ifarch %{arm} ppc64le %{ix86}
%global run_valgrind_tests OFF
%endif
# Turn off valgrind unilaterally on all arches which don't have
# valgrind at all, like riscv64.
%ifnarch %{valgrind_arches}
%global run_valgrind_tests OFF
%endif

Name: libyang
Version: 3.13.5
Release: 2%{?dist}
Summary: YANG data modeling language library
Url: https://github.com/CESNET/libyang
Source: %{url}/archive/%{name}-%{version}.tar.gz
License: BSD-3-Clause

# disable tests failing on s390x
Patch1: disable-test_structure.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  cmake(cmocka) >= 1.0.1
BuildRequires:  make
BuildRequires:  git-core
BuildRequires:  pkgconfig(libpcre2-8) >= 10.21
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif

Conflicts:      %{name} < 1.0.225-3

%package devel
Summary:    Development files for libyang
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pcre2-devel

%package devel-doc
Summary:    Documentation of libyang API
Requires:   %{name}%{?_isa} = %{version}-%{release}

%package tools
Summary:        YANG validator tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
# This was not properly split out before
Conflicts:      %{name} < 1.0.225-3 

%description devel
Headers of libyang library.

%description devel-doc
Documentation of libyang API.

%description tools
YANG validator tools.

%description
Libyang is YANG data modeling language parser and toolkit
written (and providing API) in C.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -S git

%build
%cmake \
   -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
   -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
   -DENABLE_LYD_PRIV=ON \
   -DENABLE_VALGRIND_TESTS=%{run_valgrind_tests}
%cmake_build

%cmake_build -t doc

%check
pushd redhat-linux-build
ctest --output-on-failure -V %{?_smp_mflags}
popd

%install
%cmake_install

mkdir -m0755 -p %{buildroot}/%{_docdir}/libyang
cp -a doc/html %{buildroot}/%{_docdir}/libyang/html

%files
%license LICENSE
%{_libdir}/libyang.so.3
%{_libdir}/libyang.so.3.*
%{_datadir}/yang/modules/libyang/*.yang
%dir %{_datadir}/yang/
%dir %{_datadir}/yang/modules/
%dir %{_datadir}/yang/modules/libyang/

%files tools
%{_bindir}/yanglint
%{_bindir}/yangre
%{_datadir}/man/man1/yanglint.1.gz
%{_datadir}/man/man1/yangre.1.gz

%files devel
%{_libdir}/libyang.so
%{_libdir}/pkgconfig/libyang.pc
%{_includedir}/libyang/*.h
%dir %{_includedir}/libyang/

%files devel-doc
%{_docdir}/libyang

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.13.5-2
- Import
