%global source1_hash fcc6a14f8478a14061d0caa66703810c0b4fc851c63afde10a117b700dc1fcba
%global source0_hash 8892439e5570091965aaffe30b08631fdf7ca7f81f6495b4648f0950d7ea7963

# Parallel build broken
%global _smp_mflags -j1

%bcond_with java

%if 0%{?fedora}
%bcond_without mingw
%else
%bcond_with mingw
%endif

Name:           libkml
Version:        1.3.0
Release:        58%{?dist}
Summary:        Reference implementation of OGC KML 2.2

License:        BSD-3-Clause
URL:            https://github.com/libkml/libkml
Source0:        https://github.com/libkml/libkml/archive/%{version}/libkml-%{version}.tar.gz
# TODO: Port to minizip-2.x, meanwhile bundle version 1.3.0
# wget -O minizip-1.3.0.tar.gz http://sourceforge.net/projects/libkml-files/files/1.3.0/minizip.tar.gz/download
Source1:        https://downloads.sourceforge.net/project/libkml-files/1.3.0/minizip.tar.gz#/minizip-1.3.0.tar.gz

## See https://github.com/libkml/libkml/pull/239
Patch0:         0001-Fix-build-failure-due-to-failure-to-convert-pointer-.patch
Patch1:         0002-Fix-mistaken-use-of-std-cerr-instead-of-std-endl.patch
Patch2:         0003-Fix-python-tests.patch
Patch3:         0004-Correctly-build-and-run-java-test.patch
# Fix a fragile test failing on i686
Patch4:         fragile_test.patch
# Don't bytecompile python sources as part of build process, leave it to rpmbuild
Patch5:         libkml_dont-bytecompile.patch
# Add crypt.h which was removed from Fedora minizip package (see #1424609)
Patch6:         libkml_crypth.patch
# Use local file for bundled minizip
Patch7:         libkml-bundle-minizip.patch
# Fix possible OOB array access in strcmp due to undersized array
Patch8:         libkml_test_strcmp.patch
# MinGW build fixes
Patch9:         libkml_mingw.patch
# Increase minimum cmake version
Patch10:        libkml_cmakever.patch
Patch11:        libkml-boost-intrusive-ptr.patch

BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  boost-devel
BuildRequires:  expat-devel
BuildRequires:  gtest-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  uriparser-devel
BuildRequires:  zlib-devel
%if %{with java}
BuildRequires:  java-devel
BuildRequires:  junit
%endif

%if %{with mingw}
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-boost
BuildRequires:  mingw32-curl
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-uriparser
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-boost
BuildRequires:  mingw64-curl
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-uriparser
BuildRequires:  mingw64-zlib
%endif

Provides:       bundled(minizip) = 1.3.0

%global __requires_exclude_from ^%{_docdir}/.*$
%global __provides_exclude_from ^%{python3_sitearch}/.*\\.so$

%description
Reference implementation of OGC KML 2.2.
It also includes implementations of Google's gx: extensions used by Google
Earth, as well as several utility libraries for working with other formats.

%package -n python3-%{name}
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
The python3-%{name} package contains Python 3 bindings for %{name}.

%if %{with java}
%package java
Summary:        Java bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description java
The %{name}-java package contains Java bindings for %{name}.
%endif

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       expat-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:        MinGW Windows %{name} library
Requires:       mingw32-boost
BuildArch:      noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw32-python3-%{name}
Summary:        MinGW Windows Python 3 %{name} library
Requires:       mingw32-%{name} = %{version}-%{release}
BuildArch:      noarch

%description -n mingw32-python3-%{name}
MinGW Windows Python 3 %{name} library.

%package -n mingw64-%{name}
Summary:        MinGW Windows %{name} library
Requires:       mingw64-boost
BuildArch:      noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.

%package -n mingw64-python3-%{name}
Summary:        MinGW Windows Python 3 %{name} library
Requires:       mingw64-%{name} = %{version}-%{release}
BuildArch:      noarch

%description -n mingw64-python3-%{name}
MinGW Windows Python 3 %{name} library.

%{?mingw_debug_package}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a1

%build
# Build bundled minizip
pushd minizip
(
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DBUILD_SHARED_LIBS=OFF
%cmake_build
)

%if %{with mingw}
(
%mingw_cmake -DBUILD_SHARED_LIBS=OFF
%mingw_make_build
)
%endif
popd

# Native build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DWITH_SWIG=ON -DWITH_PYTHON=ON \
%if %{with java}
  -DWITH_JAVA=ON -DJNI_INSTALL_DIR=%{_libdir}/%{name} \
%endif
  -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/%{name} \
  -DINCLUDE_INSTALL_DIR=%{_includedir}/kml \
  -DLIB_INSTALL_DIR=%{_libdir} \
  -DPYTHON_LIBRARY=%{_usr}/%{_lib}/libpython%{python3_version}$(python3-config --abiflags).so \
  -DPYTHON_INCLUDE_DIR=%{_usr}/include/python%{python3_version}$(python3-config --abiflags)/ \
  -DPYTHON_INSTALL_DIR=%{python3_sitearch} \
  -DMINIZIP_INCLUDE_DIR=$PWD -DMINIZIP_LIBRARY=$PWD/minizip/%{_vpath_builddir}/libminizip.a \
  -DBUILD_TESTING=ON \
  -DBUILD_EXAMPLES=ON
%cmake_build

%if %{with mingw}
export MINGW32_CMAKE_ARGS="\
  -DCMAKE_INSTALL_DIR=%{mingw32_libdir}/cmake/%{name} \
  -DINCLUDE_INSTALL_DIR=%{mingw32_includedir}/kml \
  -DLIB_INSTALL_DIR=%{mingw32_libdir} \
  -DPYTHON_LIBRARY=%{mingw32_libdir}/libpython%{mingw32_python3_version}.dll.a \
  -DPYTHON_INCLUDE_DIR=%{mingw32_includedir}/python%{mingw32_python3_version}/ \
  -DPYTHON_INSTALL_DIR=%{mingw32_python3_sitearch} \
  -DMINIZIP_INCLUDE_DIR=$PWD -DMINIZIP_LIBRARY=$PWD/minizip/build_win32/libminizip.a"

export MINGW64_CMAKE_ARGS="\
  -DCMAKE_INSTALL_DIR=%{mingw64_libdir}/cmake/%{name} \
  -DINCLUDE_INSTALL_DIR=%{mingw64_includedir}/kml \
  -DLIB_INSTALL_DIR=%{mingw64_libdir} \
  -DPYTHON_LIBRARY=%{mingw64_libdir}/libpython%{mingw64_python3_version}.dll.a \
  -DPYTHON_INCLUDE_DIR=%{mingw64_includedir}/python%{mingw64_python3_version}/ \
  -DPYTHON_INSTALL_DIR=%{mingw64_python3_sitearch} \
  -DMINIZIP_INCLUDE_DIR=$PWD -DMINIZIP_LIBRARY=$PWD/minizip/build_win64/libminizip.a"

# MinGW build
%mingw_cmake -DWITH_SWIG=ON -DWITH_PYTHON=ON \
  -DBUILD_TESTING=OFF \
  -DBUILD_EXAMPLES=OFF
%mingw_make_build
%endif

%install
%cmake_install

%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post
%endif

%check
%ctest

%files
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/libkml*.so.*

%files -n python3-%{name}
%{python3_sitearch}/*.so
%{python3_sitearch}/*.py
%{python3_sitearch}/__pycache__/*.pyc

%if %{with java}
%files java
%{_javadir}/LibKML.jar
%{_libdir}/%{name}/
%endif

%files devel
%doc examples
%{_includedir}/kml/
%{_libdir}/libkml*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%if %{with mingw}
%files -n mingw32-%{name}
%license LICENSE
%{mingw32_bindir}/%{name}*.dll
%{mingw32_includedir}/kml/
%{mingw32_libdir}/%{name}*.dll.a
%{mingw32_libdir}/pkgconfig/%{name}.pc
%{mingw32_libdir}/cmake/%{name}/

%files -n mingw32-python3-%{name}
%{mingw32_python3_sitearch}/*.py*

%files -n mingw64-%{name}
%license LICENSE
%{mingw64_bindir}/%{name}*.dll
%{mingw64_includedir}/kml/
%{mingw64_libdir}/%{name}*.dll.a
%{mingw64_libdir}/pkgconfig/%{name}.pc
%{mingw64_libdir}/cmake/%{name}/

%files -n mingw64-python3-%{name}
%{mingw64_python3_sitearch}/*.py*
%endif

%changelog
%autochangelog
