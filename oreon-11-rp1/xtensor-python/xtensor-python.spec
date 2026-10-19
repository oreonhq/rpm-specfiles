%global source0_hash 3be09f2bc284e5a468937ad411a9976f9ab7ea5d0df40f5b1964a3694e7ee931
%undefine __cmake_in_source_build
Name:           xtensor-python
Version:        0.29.0
Release:        1%{?dist}
Summary:        Python bindings for xtensor
License:        LicenseRef-Callaway-BSD
URL:            https://xtensor-python.readthedocs.io/
%global github  https://github.com/QuantStack/xtensor-python
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{github}/pull/324.diff
Patch1:         %{github}/pull/326.diff
Patch2:         %{github}/pull/325.diff
Patch3:         %{github}/pull/327.diff
ExcludeArch:    armv7hl ppc64le s390x
%global debug_package %{nil}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  xtensor-devel
# /oreon:deps
%description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Requires:       pybind11-devel
Requires:       python3-devel
Requires:       xtensor-devel
Requires:       python3-numpy
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

%make_build -C %{_vpath_builddir} xtest
%files -f %{oreon_filedir}/main.list
%files -n xtensor-python-devel -f %{oreon_filedir}/xtensor-python-devel.list

%changelog

%autochangelog
