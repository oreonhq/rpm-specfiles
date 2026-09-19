%global source0_hash none

# Workaround for GCC-10
%define _legacy_common_support 1

%global commit %{nil}
%global shortcommit %{nil}
%global datecommit %{nil}

# To perform all tests, APBS needs to be compiled together additional sub-modules
%bcond check 0

Name: apbs
Summary: Adaptive Poisson Boltzmann Solver
Version: 3.0.0
Release: 34%{datecommit}%{shortcommit}%{?dist}
# iAPBS looks licensed with a LGPLv2+, APBS is released under BSD license.
License: LGPL-2.0-or-later AND BSD-3-Clause
URL: https://www.poissonboltzmann.org/
Source0: https://github.com/Electrostatics/apbs/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}-LGPL_V2

Patch0: %{name}-cmake.patch

# Exclude tests because they are for features inactivated
Patch1: %{name}-exclude_tests.patch

# Porting to Python-3.11
Patch2: %{name}-python311.patch

Patch3: apbs-c99.patch

BuildRequires: gcc-c++
BuildRequires: cmake3
BuildRequires: chrpath
BuildRequires: make
BuildRequires: doxygen
BuildRequires: doxygen-latex
BuildRequires: graphviz
BuildRequires: maloc-devel
BuildRequires: zlib-devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: python3-%{name}

%description
APBS is a software package for the numerical solution of the
Poisson-Boltzmann equation (PBE), one of the most popular continuum
models for describing electrostatic interactions between molecular
solutes in salty, aqueous media.  APBS was designed to efficiently
evaluate electrostatic properties for such simulations for a wide
range of length scales to enable the investigation of molecules with
tens to millions of atoms. It is also widely used in molecular
visualization (in such applications as PyMOL).

%package tools
Summary: Utility programs that utilize the APBS package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
The apbs-tools package contains several utility programs for
conversion, analysis and preparation of files that use the adaptive
poisson boltzmann solver library.

%package libs
Summary: Libraries for APBS
%description libs
APBS solver libraries.

%package devel
Summary: Libraries and header files for the APBS package
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The apbs-devel package contains the header files and libraries
necessary for developing programs using the adaptive poisson boltzmann
(APBS) solver library.

%package doc
Summary: Documentation for the APBS package
BuildRequires: tex(latex)
BuildRequires: texlive-multirow
BuildRequires: texlive-hanging
BuildRequires: texlive-adjustbox
BuildRequires: texlive-stackengine
BuildRequires: texlive-sectsty
BuildRequires: texlive-etoc
BuildRequires: texlive-tocloft
BuildRequires: texlive-ulem
BuildRequires: texlive-newunicodechar
BuildRequires: texlive-wasy
BuildRequires: texlive-wasysym
BuildArch: noarch
%description doc
The apbs-doc package contains API reference inforemation for
development using the adaptive poisson boltzmann (APBS) solver
library.

%package -n python3-apbs
Summary: Python interface of APBS
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-sphinx
BuildRequires: swig
%{?python_provide:%python_provide python3-%{name}}
Obsoletes:     %{name}-libs < 0:3.0.0-11
%description -n python3-apbs
Python interface of APBS.

%prep
%autosetup -n %{name}-%{version} -N
%patch -P 0 -p2 -b .apbs-cmake
%patch -P 1 -p1 -b .exclude_tests

%if 0%{?python3_version_nodots} >= 311
%patch -P 2 -p1 -b .python311
%endif

%patch -P 3 -p1

cp -p contrib/iapbs/COPYING contrib/iapbs/iapbs-COPYING
cp -p %{SOURCE1} contrib/iapbs/iapbs-LGPLv2

%build
export CFLAGS="%{build_cflags} -fopenmp -lm"
export CXXFLAGS="%{build_cxxflags} -fopenmp -lm"
%cmake -DCMAKE_BUILD_TYPE:STRING=Release \
 -DENABLE_iAPBS:BOOL=ON -DENABLE_OPENMP:BOOL=ON -DENABLE_VERBOSE_DEBUG:BOOL=OFF \
 -DENABLE_FETK:BOOL=OFF -DCMAKE_C_FLAGS:STRING="%{build_cflags} -fopenmp -lm -DNDEBUG" \
 -DCMAKE_CXX_FLAGS:STRING="%{build_cxxflags} -fopenmp -lm -DNDEBUG" \
 -DENABLE_PYTHON:BOOL=ON -DBUILD_DOC:BOOL=ON \
 -DBUILD_TESTING:BOOL=ON -DENABLE_TESTS:BOOL=ON \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
 -DLIB_INSTALL_DIR:PATH=%{_libdir} \
 -DSHARE_INSTALL_PREFIX:PATH=%{_datadir}

%cmake_build

%install
%cmake_install

# Tools
for bin in %{buildroot}%{_bindir}/{coulomb,born,mgmesh,dxmath,mergedx2,mergedx,value,uhbd_asc2bin,smooth,dx2mol,dx2uhbd,similarity,multivalue,benchmark,analysis,del2dx,tensor2dx}; do
    cp -p $bin %{buildroot}%{_bindir}/apbs-`basename $bin`
    rm -f $bin
done

# Remove rpaths
for bin in %{buildroot}%{_bindir}/apbs-{coulomb,born,mgmesh,dxmath,mergedx2,mergedx,value,uhbd_asc2bin,smooth,dx2mol,dx2uhbd,similarity,multivalue,benchmark,analysis,del2dx,tensor2dx}; do
    chrpath -d $bin
    chrpath -d %{buildroot}%{_bindir}/apbs
done

chrpath -d %{buildroot}%{_libdir}/libapbs.so.1

# Move Python libraries under Python's tree directories
mkdir -p %{buildroot}%{python3_sitearch}/apbs
install -pm 755 tools/manip/psize.py %{buildroot}%{python3_sitearch}/apbs/
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/apbs/psize.py
ln -s %{python3_sitearch}/apbs/psize.py %{buildroot}%{_bindir}/apbs-psize.py
install -pm 755 %_vpath_builddir/lib/_apbslib.so %{buildroot}%{python3_sitearch}/apbs/

# Remove redundant tools binary files in /usr/share
rm -rf %{buildroot}%{_datadir}/apbs

# Remove static libraries
for i in `find %{buildroot} -type f \( -name "*.a" \)`; do
 rm -f $i
done

%if %{with check}
%check
pushd tests
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export PATH=%{buildroot}%{_bindir}
%{__python3} ./apbs_tester.py
%endif

%files
%{_bindir}/apbs

%files libs
%license LICENSE.md COPYING contrib/iapbs/iapbs-COPYING contrib/iapbs/iapbs-LGPLv2
%doc README.md
%{_libdir}/libapbs.so.1

%files -n python3-apbs
%{python3_sitearch}/apbs/

%files devel
%{_libdir}/libapbs.so
%{_includedir}/iapbs/
%{_includedir}/apbs

%files tools
%{_bindir}/apbs-psize.py
%{_bindir}/apbs-coulomb
%{_bindir}/apbs-born
%{_bindir}/apbs-mgmesh
%{_bindir}/apbs-dxmath
%{_bindir}/apbs-mergedx2
%{_bindir}/apbs-mergedx
%{_bindir}/apbs-value
%{_bindir}/apbs-uhbd_asc2bin
%{_bindir}/apbs-smooth
%{_bindir}/apbs-dx2mol
%{_bindir}/apbs-dx2uhbd
%{_bindir}/apbs-similarity
%{_bindir}/apbs-multivalue
%{_bindir}/apbs-benchmark
%{_bindir}/apbs-analysis
%{_bindir}/apbs-del2dx
%{_bindir}/apbs-tensor2dx

%files doc
%license LICENSE.md
%doc %_vpath_builddir/doc

%changelog
%autochangelog
