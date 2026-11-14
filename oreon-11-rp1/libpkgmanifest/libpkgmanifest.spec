# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: LGPL-2.1-or-later

%global source0_hash 05deb3f91fee952c342f8a2861d5840bf41178a94e2e4d97acf51aa896b7ab98

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_with docs
%bcond_without python
%bcond_without tests

Name: libpkgmanifest
Version: 0.6.2
Release: 1%{?dist}
Summary: Library for working with RPM manifests
License: LGPL-2.1-or-later
URL: https://github.com/rpm-software-management/libpkgmanifest
Source0: https://github.com/rpm-software-management/libpkgmanifest/archive/v%{version}/libpkgmanifest-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(yaml-cpp) >= 0.7.0
BuildRequires: pkgconfig(rpm)
%if %{with tests}
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(gtest)
%endif
%if %{with python}
BuildRequires: python3-devel
BuildRequires: swig
%endif
%if %{with docs}
BuildRequires: doxygen
BuildRequires: python3dist(breathe)
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(sphinx-rtd-theme)
%endif

%description
libpkgmanifest parses and generates RPM package manifest files.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libpkgmanifest) = %{version}

%description devel
Headers and pkgconfig for %{name}.

%if %{with python}
%package -n python3-libpkgmanifest
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-libpkgmanifest
Python 3 bindings for %{name}.
%endif

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake \
  -DWITH_DOCS=%{?with_docs:ON}%{!?with_docs:OFF} \
  -DWITH_PYTHON=%{?with_python:ON}%{!?with_python:OFF} \
  -DWITH_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
  -DWITH_CODE_COVERAGE=OFF \
  -DVERSION_MAJOR=0 \
  -DVERSION_MINOR=6 \
  -DVERSION_PATCH=2
%cmake_build

%install
%cmake_install

%check
%if %{with tests}
%ctest
%endif

%files
%license COPYING.LIB
%doc README.md
%{_libdir}/libpkgmanifest.so.0
%{_libdir}/libpkgmanifest.so.0.*

%files devel
%{_libdir}/libpkgmanifest.so
%{_includedir}/libpkgmanifest/
%{_libdir}/pkgconfig/libpkgmanifest.pc

%if %{with python}
%files -n python3-libpkgmanifest
%{python3_sitearch}/libpkgmanifest
%{python3_sitearch}/libpkgmanifest-*.dist-info
%endif

%changelog
%autochangelog
