%global source0_hash 2b4f76d479490b6b503217bb8135cf05a924c22fc8307e6829b82a586f67d3c1

%bcond check 0
%bcond_without python

ExcludeArch:   %{ix86}

Name:           libCombine
Summary:        C++ library for working with the COMBINE Archive format
Version:        0.2.20
Release:        15%{?dist}
URL:            https://github.com/sbmlteam/libCombine
Source0:        %{url}/archive/%{version}/libCombine-%{version}.tar.gz

# Header files and part of source code is released under LGPLv2+ license
License:        BSD-2-Clause and LGPL-2.0-or-later

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libsbml-devel
BuildRequires: libnuml-devel
BuildRequires: expat-devel
BuildRequires: libxml2-devel
BuildRequires: bzip2-devel
BuildRequires: xerces-c-devel
BuildRequires: zlib-devel
BuildRequires: zipper-devel
BuildRequires: minizip-devel >= 2.5.0

Patch0: libCombine-set-external-library-names.patch
Patch1: libCombine-pull67.patch

%description
LibCombine implements a C++ API library providing support for the
Combine Archive. The library is written after the likeness of
libSBML (and in fact some classes have been generated using DEVISER).
Thus even thought he core is written in C++, the classes can be
accessed via SWIG from .NET, Java and Python.

%package devel
Summary: Development files of %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libsbml-devel%{?_isa}

%description devel
This package provides header, shared and static library files
of %{name}.

%package static
Summary: Static library of %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package provides static library file of %{name}.

%if %{with python}
%package -n python3-%{name}
BuildRequires:  python3-devel, swig
BuildRequires:  python3-setuptools
BuildRequires: make
Summary:  Python 3 bindings for libCombine
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: swig

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package contains %{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libCombine-%{version} -p1

%build
%cmake -Wno-dev -Wno-cpp -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DLIBCOMBINE_SHARED_VERSION:BOOL=ON -DLIBCOMBINE_SKIP_SHARED_LIBRARY:BOOL=OFF \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON -DWITH_CHECK:BOOL=ON \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES -Dsbml-static_DIR:PATH=%{_libdir}/cmake \
 -DLIBSBML_LIBRARY:FILEPATH=%{_libdir}/libsbml.so -DLIBSBML_SHARED:BOOL=ON \
 -DZIPPER_LIBRARY:FILEPATH=%{_libdir}/libZipper.so \
 -DZIPPER_INCLUDE_DIR:PATH=%{_includedir}/zipper -DEXTRA_LIBS:STRING="numl;sbml;xml2;bz2;z;m;dl;expat" \
 -DEXTRA_INCLUDE:STRING=%{_includedir}/libxml2 \
%if %{with python}
 -DWITH_PYTHON:BOOL=ON \
 -DPYTHON_INCLUDE_DIR:PATH=%{_includedir}/python%{python3_version}$(python3-config --abiflags) \
 -DPYTHON_LIBRARY:FILEPATH=%{_libdir}/libpython%{python3_version}$(python3-config --abiflags).so \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3}
%endif

%cmake_build

%install
%cmake3_install

rm -rf %{buildroot}%{_datadir}

%if %{with check}
%check
%ctest
%endif

%files
%doc README.md VERSION.txt
%license LICENSE.md
%{_libdir}/libCombine.so.0
%{_libdir}/libCombine.so.%{version}

%files devel
%{_libdir}/libCombine.so
%{_libdir}/cmake/Combine-config-*.cmake
%{_libdir}/cmake/Combine-config.cmake
%{_libdir}/cmake/Combine-targets.cmake
%{_libdir}/cmake/Combine-targets-*.cmake
%{_includedir}/combine/
%{_includedir}/omex/

%files static
%{_libdir}/libCombine-static.a
%{_libdir}/cmake/Combine-static-*.cmake

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/libcombine.pth
%{python3_sitearch}/libcombine/
%endif

%changelog
%autochangelog
