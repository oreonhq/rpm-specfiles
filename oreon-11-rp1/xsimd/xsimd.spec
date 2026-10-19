%global source0_hash b3d50e7a73fbf4642ceef30131c93414901d69eee41c2a5302db650b03e2c792
Name:           xsimd
Version:        14.3.0
Release:        1%{?dist}
Summary:        C++ wrappers for SIMD intrinsic
License:        BSD-3-Clause
URL:            https://xsimd.readthedocs.io/
%global github  https://github.com/xtensor-stack/xsimd
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz
%global debug_package %{nil}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  gcc-c++
# /oreon:deps
%description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch
%description devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_TESTS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifnarch ppc64le s390x
%cmake_build -- xtest
%endif
%files -f %{oreon_filedir}/main.list
%files -n xsimd-devel -f %{oreon_filedir}/xsimd-devel.list

%changelog

%autochangelog
