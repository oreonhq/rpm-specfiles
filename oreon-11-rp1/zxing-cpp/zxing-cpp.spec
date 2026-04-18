Name:           zxing-cpp
Version:        2.2.1
Release:        %autorelease
Summary:        C++ port of the ZXing ("Zebra Crossing") barcode scanning library

# The entire source is ASL 2.0, except:
# - wrappers/wasm/base64ArrayBuffer.js is MIT (but is not used)
License:        Apache-2.0 AND MIT
URL:            https://github.com/zxing-cpp/zxing-cpp
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
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
%autosetup -p1

# don’t use unversioned “python” interpreter in tests
sed -r -i 's@(COMMAND )python@\1%{python3}@' wrappers/python/CMakeLists.txt
# we don’t need cmake as a python dependency
sed -r -i '/cmake/d' wrappers/python/pyproject.toml

sed -i 's/pybind11\[global\]/pybind11/' wrappers/python/pyproject.toml
# build verbosely:

%generate_buildrequires
pushd wrappers/python &>/dev/null
%pyproject_buildrequires -r
popd &>/dev/null

%build
# Setting BUILD_PYTHON_MODULE builds a Python extension shared library module,
# but we don’t get any metadata (dist-info), so it’s not terribly useful for
# packaging purposes. Instead, it seems we must re-build the whole library
# through setuptools to get that.
# CMAKE_BUILD_TYPE=RelWithDebInfo prevents the build from stripping the
# python module after it is built.  The stripping happens in
# pybind11_add_module.
%cmake \
    -DZXING_DEPENDENCIES=LOCAL \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_PYTHON_MODULE=ON \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
pushd wrappers/python
# CMake respects this environment variable. We need to see the compiler
# invocations to verify the distro build flags are respected. Unfortunately,
# pybind11 does add -O3, and there doesn’t seem to be a way to turn that off.
# It’s a global pybind11 decision, not something in this package’s sources.
export VERBOSE=1
%pyproject_wheel
popd

%install
%cmake_install
pushd wrappers/python
%pyproject_install
# Now we do something sneaky: we substitute the Python extension that was built
# in the original CMake invocation, replacing the one built with setuptools. It
# is dynamically linked against the main libZXing.so, which makes it smaller,
# and it was not built with that pesky -O3 that was added by pybind11, so it
# better complies with packaging guidelines. The only problem is it contains an
# rpath that we need to remove.
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
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.1-%autorelease
- Import from Fedora dist-git f43 for Oreon 11
