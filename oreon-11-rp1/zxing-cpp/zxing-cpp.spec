%global source0_hash 7286b1e6ade66fe82b7c8208b4595deeb55d6486b410834fdc65702f46650542
Name:           zxing-cpp
Version:        3.1.1
Release:        1%{?dist}
Summary:        C++ port of the ZXing ("Zebra Crossing") barcode scanning library
License:        Apache-2.0 AND MIT
URL:            https://github.com/zxing-cpp/zxing-cpp
Source0:        https://codeload.github.com/zxing-cpp/zxing-cpp/tar.gz/refs/tags/v%{version}#/zxing-cpp-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(nanobind) >= 2.11.0
BuildRequires:  python3dist(scikit-build-core) >= 0.12
BuildRequires:  python3dist(typing-extensions) >= 4.12
Requires:       python3-zxing-cpp = %{version}-%{release}
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# don’t use unversioned “python” interpreter in tests
sed -r -i 's@(COMMAND )python@\1%{python3}@' wrappers/python/CMakeLists.txt
# we don’t need cmake as a python dependency
sed -r -i '/cmake/d' wrappers/python/pyproject.toml

sed -i 's/pybind11\[global\]/pybind11/' wrappers/python/pyproject.toml
# build verbosely:

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
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/zxing_cpp* usr/lib64/python3*/site-packages/zxing_cpp* usr/bin/*

%check

%ctest
%files
%files -n zxing-cpp-devel -f %{oreon_filedir}/zxing-cpp-devel.list
%files -n python3-zxing-cpp -f %{oreon_filedir}/python3-zxing-cpp.list

%changelog

* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.1-%autorelease
- Import from Fedora dist-git f43 for Oreon 11
