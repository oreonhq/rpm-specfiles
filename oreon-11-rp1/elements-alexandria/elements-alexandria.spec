%global source0_hash 74497287b96d370afd59577792e0c45a7b2b4c85babc8d108727746641828efa

Summary:        A lightweight C++ utility library
Name:           elements-alexandria
Version:        2.32.0
Release:        6%{?dist}
# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:        LGPL-3.0-or-later
URL:            https://github.com/astrorama/Alexandria
Source0:        https://github.com/astrorama/Alexandria/archive/%{version}/%{name}-%{version}.tar.gz
# This file is used to link the documentation to cppreference.com
# It is downloaded from:
# https://upload.cppreference.com/w/File:cppreference-doxygen-web.tag.xml
Source1:        cppreference-doxygen-web.tag.xml
Patch0:         boost-1.90-headers.patch

%global elements_version 6.3.4

BuildRequires: CCfits-devel
BuildRequires: boost-devel >= 1.53
BuildRequires: cfitsio-devel
BuildRequires: cppunit-devel
BuildRequires: elements-devel = %{elements_version}
BuildRequires: log4cpp-devel
# Required for the generation of the documentation
BuildRequires: elements-doc = %{elements_version}
BuildRequires: doxygen
BuildRequires: graphviz

BuildRequires: gcc-c++ > 4.7
BuildRequires: cmake >= 2.8.5
%if 0%{?fedora} >= 30
BuildRequires: python3
BuildRequires: python3-pytest
BuildRequires: python3-devel
%else
BuildRequires: python2
BuildRequires: python2-pytest
BuildRequires: python2-devel
%endif
BuildRequires: make

%if 0%{?rhel} && 0%{?rhel} <= 7
Requires: cmake%{?_isa}
%else
Requires: cmake-filesystem%{?_isa}
%endif

%global cmakedir %{_libdir}/cmake/ElementsProject

%global makedir %{_datadir}/Elements/make
%global confdir %{_datadir}/Elements
%global auxdir %{_datadir}/auxdir
%global docdir %{_docdir}/Alexandria

%if 0%{?fedora} >= 30
%global python_sitearch %{python3_sitearch}
%else
%global python_sitearch %{python2_sitearch}
%endif

%description
A lightweight C++ utility library.

%package devel
Summary: The development part of the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: elements-devel%{?_isa} = %{elements_version}

%description devel
The development part of the %{name} package.

%package doc
Summary: Documentation for package %{name}
# Automatically converted from old format: LGPLv3+ and CC-BY-SA - review is highly recommended.
License: LGPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
BuildArch: noarch
Requires: elements-doc = %{elements_version}

%description doc
Documentation for package %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Alexandria-%{version} -p1

%build
export VERBOSE=1
EXTRA_CMAKE_FLAGS="-DUSE_ENV_FLAGS=ON"
%if 0%{?fedora} >= 30
EXTRA_CMAKE_FLAGS="${EXTRA_CMAKE_FLAGS} -DPYTHON_EXPLICIT_VERSION=3"
%else
EXTRA_CMAKE_FLAGS="${EXTRA_CMAKE_FLAGS} -DPYTHON_EXPLICIT_VERSION=2"
%endif
# Build
%cmake -B "%{_vpath_builddir}" -DELEMENTS_BUILD_TESTS=ON -DELEMENTS_INSTALL_TESTS=OFF -DSQUEEZED_INSTALL:BOOL=ON -DINSTALL_DOC:BOOL=ON \
    -DUSE_SPHINX=OFF --no-warn-unused-cli \
    -DCMAKE_LIB_INSTALL_SUFFIX=%{_lib} -DUSE_VERSIONED_LIBRARIES=ON ${EXTRA_CMAKE_FLAGS}
# Copy cppreference-doxygen-web.tag.xml into the build directory
mkdir -p "%{_vpath_builddir}/doc/doxygen"
cp -v "%{SOURCE1}" "%{_vpath_builddir}/doc/doxygen"

%make_build -C "%{_vpath_builddir}"

%install
export VERBOSE=1
%make_install -C "%{_vpath_builddir}"
rm -fv "%{buildroot}/%{_libdir}/"*BoostTest.so*

%check
make test -C "%{_vpath_builddir}"

%files
%license LICENSE
%{cmakedir}/AlexandriaEnvironment.xml

%{_bindir}/AlexandriaVersion

%{_libdir}/libAlexandriaKernel.so.%{version}
%{_libdir}/libConfiguration.so.%{version}
%{_libdir}/libFilePool.so.%{version}
%{_libdir}/libGridContainer.so.%{version}
%{_libdir}/libHistogram.so.%{version}
%{_libdir}/libKdTree.so.%{version}
%{_libdir}/libMathUtils.so.%{version}
%{_libdir}/libNdArray.so.%{version}
%{_libdir}/libPhysicsUtils.so.%{version}
%{_libdir}/libPyston.so.%{version}
%{_libdir}/libSOM.so.%{version}
%{_libdir}/libSourceCatalog.so.%{version}
%{_libdir}/libTable.so.%{version}
%{_libdir}/libXYDataset.so.%{version}

%{python_sitearch}/ALEXANDRIA_VERSION.py*
%{python_sitearch}/ALEXANDRIA_INSTALL.py*
%if 0%{?fedora} >= 30
%{python_sitearch}/__pycache__/ALEXANDRIA*.pyc
%endif

%files devel
%{_libdir}/libAlexandriaKernel.so
%{_libdir}/libConfiguration.so
%{_libdir}/libFilePool.so
%{_libdir}/libGridContainer.so
%{_libdir}/libHistogram.so
%{_libdir}/libKdTree.so
%{_libdir}/libMathUtils.so
%{_libdir}/libNdArray.so
%{_libdir}/libPhysicsUtils.so
%{_libdir}/libPyston.so
%{_libdir}/libSOM.so
%{_libdir}/libSourceCatalog.so
%{_libdir}/libTable.so
%{_libdir}/libXYDataset.so

%{_includedir}/ALEXANDRIA_VERSION.h
%{_includedir}/ALEXANDRIA_INSTALL.h
%{_includedir}/AlexandriaKernel/
%{_includedir}/Configuration/
%{_includedir}/GridContainer/
%{_includedir}/FilePool/
%{_includedir}/Histogram/
%{_includedir}/KdTree/
%{_includedir}/MathUtils/
%{_includedir}/NdArray/
%{_includedir}/PhysicsUtils/
%{_includedir}/Pyston/
%{_includedir}/SOM/
%{_includedir}/SourceCatalog/
%{_includedir}/Table/
%{_includedir}/XYDataset/

%{cmakedir}/AlexandriaBuildEnvironment.xml
%{cmakedir}/AlexandriaConfig.cmake
%{cmakedir}/AlexandriaConfigVersion.cmake
%{cmakedir}/AlexandriaExports-relwithdebinfo.cmake
%{cmakedir}/AlexandriaExports.cmake
%{cmakedir}/AlexandriaKernelExport.cmake
%{cmakedir}/AlexandriaPlatformConfig.cmake
%{cmakedir}/ConfigurationExport.cmake
%{cmakedir}/FilePoolExport.cmake
%{cmakedir}/GridContainerExport.cmake
%{cmakedir}/HistogramExport.cmake
%{cmakedir}/KdTreeExport.cmake
%{cmakedir}/MathUtilsExport.cmake
%{cmakedir}/NdArrayExport.cmake
%{cmakedir}/PhysicsUtilsExport.cmake
%{cmakedir}/PystonExport.cmake
%{cmakedir}/SOMExport.cmake
%{cmakedir}/SourceCatalogExport.cmake
%{cmakedir}/TableExport.cmake
%{cmakedir}/XYDatasetExport.cmake

%files doc
%license LICENSE
%{docdir}

%changelog
%autochangelog
