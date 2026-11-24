# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 02078ae15f19f9d423a441f205b1d1bee32349ddda7467e2c84e8f08876f8635
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           zxing-cpp
Version:        2.2.1
Release:        %{autorelease}
Summary:        C++ port of the ZXing ("Zebra Crossing") barcode scanning library

License:        Apache-2.0 AND MIT
URL:            https://github.com/zxing-cpp/zxing-cpp
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(fmt)

%description
ZXing-C++ ("zebra crossing") is an open-source, multi-format 1D/2D barcode
image processing library implemented in C++.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     python3-%{name}
Summary:        Python bindings for the %{name} barcode library

BuildRequires:  python3-devel
BuildRequires:  pybind11-devel
BuildRequires:  chrpath

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
%{summary}.

%prep
%oreon_sha256
%autosetup -p1

sed -r -i 's@(COMMAND )python@\1%{python3}@' wrappers/python/CMakeLists.txt
sed -r -i '/cmake/d' wrappers/python/pyproject.toml

sed -i 's/pybind11\[global\]/pybind11/' wrappers/python/pyproject.toml

%generate_buildrequires
pushd wrappers/python &>/dev/null
%pyproject_buildrequires -r
popd &>/dev/null

%build
%cmake \
    -DZXING_DEPENDENCIES=LOCAL \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_PYTHON_MODULE=ON \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
pushd wrappers/python
export VERBOSE=1
%pyproject_wheel
popd

%install
%cmake_install
pushd wrappers/python
%pyproject_install
popd
install -t '%{buildroot}%{python3_sitearch}' -p \
    %{_vpath_builddir}/wrappers/python/zxingcpp.*.so
chrpath --delete %{buildroot}%{python3_sitearch}/zxingcpp.*.so
pushd wrappers/python
%pyproject_save_files zxingcpp
popd

%check
%ctest

%files
%license LICENSE
%{_libdir}/libZXing.so.3
%{_libdir}/libZXing.so.%{version}

%files devel
%doc README.md
%{_includedir}/ZXing/
%{_libdir}/libZXing.so
%{_libdir}/cmake/ZXing/
%{_libdir}/pkgconfig/zxing.pc

%files -n python3-%{name} -f %{pyproject_files}
%{_libdir}/zxingcpp%{python3_ext_suffix}

%changelog
%autochangelog
