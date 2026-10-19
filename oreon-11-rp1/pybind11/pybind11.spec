%global source0_hash ef712655692a2e9bf7bb7874c022564a45f91d847ddee987e720cd9e28849665
%global debug_package %{nil}
%bcond optional_tests 1
Name:    pybind11
Version: 3.1.0
Release:        1%{?dist}
Summary:        Seamless operability between C++11 and Python
License: BSD-3-Clause
URL:	 https://github.com/pybind/pybind11
Source0:        https://github.com/pybind/pybind11/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:  pybind11-2.13.6-Use_usr_prefix.patch
%if %{with optional_tests}
%endif
%global base_description \
pybind11 is a lightweight header-only library that exposes C++ types \
in Python and vice versa, mainly to create Python bindings of existing \
C++ code.
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(scikit-build-core) >= 0.11.2
Requires:       python3-pybind11 = %{version}-%{release}
# /oreon:deps
%description
%{base_description}

%package devel
Summary:  Development headers for pybind11
Provides: %{name}-static = %{version}-%{release}
%description devel
%{base_description}

This package contains the development headers for pybind11.

%package -n     python3-%{name}
Summary:        Seamless operability between C++11 and Python
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description -n python3-%{name}
%{base_description}

This package contains the Python 3 files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DUSE_PYTHON_INCLUDE_DIR=FALSE
%cmake_build
%{pyproject_wheel %{shrink:
  -C cmake.build-type=Release
  -C cmake.define.PYBIND11_INSTALL=OFF
  -C cmake.define.PYBIND11_TEST=OFF
}}
%install
%cmake_install
%pyproject_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/pybind11* usr/lib64/python3*/site-packages/pybind11* usr/bin/*

%check

%cmake_build --target check
%files
%files -n pybind11-devel -f %{oreon_filedir}/pybind11-devel.list
%files -n python3-pybind11 -f %{oreon_filedir}/python3-pybind11.list

%changelog

%autochangelog
