%global source0_hash 752f1682ed97b9e5e473dad29f533690779abbe30f8822af24977e9e98939c9b
%define _legacy_common_support 1
%global commit %{nil}
%global shortcommit %{nil}
%global datecommit %{nil}
%bcond check 0
Name: apbs
Summary:        Adaptive Poisson Boltzmann Solver
Version: 3.0.0
Release:        1%{?dist}
License: LGPL-2.0-or-later AND BSD-3-Clause
URL: https://www.poissonboltzmann.org/
Source0:        https://github.com/Electrostatics/apbs/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}-LGPL_V2
Patch0: %{name}-cmake.patch
Patch1: %{name}-exclude_tests.patch
Patch2: %{name}-python311.patch
Patch3: apbs-c99.patch
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: python3-%{name}
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  maloc-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-sphinx
BuildRequires:  swig
BuildRequires:  tex(latex)
BuildRequires:  texlive-adjustbox
BuildRequires:  texlive-etoc
BuildRequires:  texlive-hanging
BuildRequires:  texlive-multirow
BuildRequires:  texlive-newunicodechar
BuildRequires:  texlive-sectsty
BuildRequires:  texlive-stackengine
BuildRequires:  texlive-tocloft
BuildRequires:  texlive-ulem
BuildRequires:  texlive-wasy
BuildRequires:  texlive-wasysym
BuildRequires:  zlib-devel
# /oreon:deps
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
for bin in %{buildroot}%{_bindir}/{coulomb,born,mgmesh,dxmath,mergedx2,mergedx,value,uhbd_asc2bin,smooth,dx2mol,dx2uhbd,similarity,multivalue,benchmark,analysis,del2dx,tensor2dx}; do
    cp -p $bin %{buildroot}%{_bindir}/apbs-`basename $bin`
    rm -f $bin
done
for bin in %{buildroot}%{_bindir}/apbs-{coulomb,born,mgmesh,dxmath,mergedx2,mergedx,value,uhbd_asc2bin,smooth,dx2mol,dx2uhbd,similarity,multivalue,benchmark,analysis,del2dx,tensor2dx}; do
    chrpath -d $bin
    chrpath -d %{buildroot}%{_bindir}/apbs
done
chrpath -d %{buildroot}%{_libdir}/libapbs.so.1
mkdir -p %{buildroot}%{python3_sitearch}/apbs
install -pm 755 tools/manip/psize.py %{buildroot}%{python3_sitearch}/apbs/
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/apbs/psize.py
ln -s %{python3_sitearch}/apbs/psize.py %{buildroot}%{_bindir}/apbs-psize.py
install -pm 755 %_vpath_builddir/lib/_apbslib.so %{buildroot}%{python3_sitearch}/apbs/
rm -rf %{buildroot}%{_datadir}/apbs
for i in `find %{buildroot} -type f \( -name "*.a" \)`; do
 rm -f $i
done
%oreon_autofiles apbs-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles apbs-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles apbs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles apbs-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-apbs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

pushd tests
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export PATH=%{buildroot}%{_bindir}
%{__python3} ./apbs_tester.py
%endif
%files -f %{oreon_filedir}/main.list
%files -n apbs-tools -f %{oreon_filedir}/apbs-tools.list
%files -n apbs-libs -f %{oreon_filedir}/apbs-libs.list
%files -n apbs-devel -f %{oreon_filedir}/apbs-devel.list
%files -n apbs-doc -f %{oreon_filedir}/apbs-doc.list
%files -n python3-apbs -f %{oreon_filedir}/python3-apbs.list

%changelog

%autochangelog
