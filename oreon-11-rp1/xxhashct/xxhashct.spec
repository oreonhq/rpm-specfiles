%global source0_hash 5883af6ef16ce301b2544b0661696db46f2b7134de0fcd35c55cbc8226f182fc
%global commit 4816a508f696dc9aff65e7ae5fd250b5e3585cb2
%global snapdate 20250517
Name:           xxhashct
Version:        0^%{snapdate}git%{sub %{commit} 1 7}
Release:        1%{?dist}
Summary:        Compile-time xxhash implementation
License:        MIT
URL:            https://github.com/ekpyron/xxhashct
Source0:        https://github.com/ekpyron/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
%global debug_package %{nil}
%global common_description %{expand:
An implementation of the 64-bit xxhash algorithm (see
https://github.com/Cyan4973/xxHash) as C++11 constexpr expression.}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  xxhash-devel
# /oreon:deps
%description %{common_description}

%package devel
Summary:        Development files for xxhashct
BuildArch:      noarch
Provides:       xxhashct-static = %{version}-%{release}
%description devel %{common_description}

The xxhashct-devel package contains libraries and header files for developing
applications that use xxhashct.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n xxhashct-%{commit} -p1

%conf
%cmake

%build

%cmake_build
%install
install -D -p -m 0644 -t '%{buildroot}%{_includedir}' xxh32.hpp xxh64.hpp
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{_vpath_builddir}/xxhashct_tests
%files -f %{oreon_filedir}/main.list
%files -n xxhashct-devel -f %{oreon_filedir}/xxhashct-devel.list

%changelog

%autochangelog
