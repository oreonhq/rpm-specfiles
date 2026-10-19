%global source0_hash ca3ecd13005309e0322bc64a26f2960e613f2a9a9cedee845865c2d042f73b3c
%global _hardened_build 1
Name:           libvarlink
Version:        24.0.1
Release:        1%{?dist}
Summary:        Varlink C Library
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/varlink/%{name}
Source0:        https://github.com/varlink/libvarlink/archive/refs/tags/v24.0.1.tar.gz#/libvarlink-24.0.1.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glibc-langpack-de
BuildRequires:  meson
# /oreon:deps
%description
Varlink C Library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        util
Summary:        Varlink command line tools
%description    util
The %{name}-util package contains varlink command line tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%check

export LC_CTYPE=C.utf8
%ifarch ppc64le
test_list=$(%meson_test --list) 2> /dev/null
test_list=${test_list//test-symbols}
%meson_test $test_list
%else
%meson_test
%endif
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libvarlink-devel -f %{oreon_filedir}/libvarlink-devel.list
%files -n libvarlink-util -f %{oreon_filedir}/libvarlink-util.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 24.0.1-1
- Prepare for Oreon 11 (RP1)
