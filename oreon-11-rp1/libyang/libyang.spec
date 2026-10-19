%global source0_hash 6906b0f26c1d4494c5c2464313b16169ec92ccd07b45ecf3a1e9eb9cd7a55c0b
%global run_valgrind_tests ON
%ifarch %{arm} ppc64le %{ix86}
%global run_valgrind_tests OFF
%endif
%ifnarch %{valgrind_arches}
%global run_valgrind_tests OFF
%endif
Name: libyang
Version: 5.8.6
Release:        1%{?dist}
Summary:        YANG data modeling language library
Url: https://github.com/CESNET/libyang
Source0:        https://github.com/CESNET/libyang/archive/refs/tags/v%{version}.tar.gz#/libyang-%{version}.tar.gz
License: BSD-3-Clause
Patch1: disable-test_structure.patch
%ifarch %{valgrind_arches}
%endif
Conflicts:      %{name} < 1.0.225-3
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(cmocka)
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  pkgconfig(libpcre2-8)
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libyang-devel -f %{oreon_filedir}/libyang-devel.list
%files -n libyang-devel-doc -f %{oreon_filedir}/libyang-devel-doc.list
%files -n libyang-tools -f %{oreon_filedir}/libyang-tools.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.13.5-2
- Import
