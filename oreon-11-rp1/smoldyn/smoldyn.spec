%global source0_hash 916041e90182ebe5cbe95d301378379e9ee55428b054a1c53e5269f804fc4132
%global with_vtk 0
Name:  smoldyn
Summary:        A particle-based spatial stochastic simulator
Version: 2.74
Release:        1%{?dist}
License: LGPL-3.0-or-later AND GPL-3.0-only AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:   http://www.smoldyn.org
Source0:        https://github.com/ssandrews/Smoldyn/archive/refs/tags/v%{version}/Smoldyn-%{version}.tar.gz
Patch0: %{name}-fix_libpaths.patch
Patch1: %{name}-freeglut.patch
Patch2: %{name}-create_soname.patch
Patch3: %{name}-avoid_automatic_wheel.patch
%if %{?with_vtk}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: bionetgen-perl
Provides: bundled(SFMT) = 1.3.3 
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-flaky
BuildRequires:  python3-matplotlib
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  zlib-devel
# /oreon:deps
%description
Smoldyn is a computer program for cell-scale biochemical simulations.
It simulates each molecule of interest individually to capture natural
stochasticity and to yield nanometer-scale spatial resolution.
It treats other molecules implicitly, enabling it to simulate hundreds
of thousands of molecules over several minutes of real time.

Simulated molecules diffuse, react, are confined by surfaces,
and bind to membranes much as they would in a real biological system.

It is more accurate and faster than other particle-based simulators.
Smoldyn unique features include: a "virtual experimenter" who can
manipulate or measure the simulated system, support for spatial compartments,
molecules with excluded volume, and simulations in 1, 2, or 3 dimensions. 

%package doc
Summary: %{name} documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
%{name} documentation.

%package libs
Summary: %{name} libraries
%description libs
%{name} shared libraries.

%package libs-devel
Summary: %{name} libraries for development
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}-libs-static = 0:%{version}-%{release}
%description libs-devel
%{name} shared and static libraries for development.

%package -n python3-smoldyn
Summary: %{name} libraries for Python
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: pybind11-devel
Requires: python3-numpy
BuildRequires: python3-matplotlib
BuildRequires: python3-flaky
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-smoldyn
%{name} libraries for Python.

%prep

%autosetup -n Smoldyn-%{version} -N
%patch -P 0 -p0 -b .fix_libpaths
%patch -P 1 -p0 -b .freeglut
%patch -P 2 -p0 -b .create_soname
%patch -P 3 -p0 -b .avoid_automatic_wheel

# Remove bundled archives
rm -rf source/MSVClibs
rm -rf source/pybind11

# Remove bundled libraries
rm -rf source/BioNetGen source/MinGWlibs Toolchain-mingw32.cmake
rm -rf source/vcell/* source/NextSubVolume/Eigen
rm -rf source/NextSubVolume/boost_include
%if !%{?with_vtk}
rm -f source/vtk/*
%endif

#Fix permissions
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.c" -exec chmod 0644 '{}' \;
find . -type f -name "*.pdf" -exec chmod 0644 '{}' \;
find . -type f -name "*.txt" -exec chmod 0644 '{}' \;
find . -type f -name "*.txt" -exec sed -i 's/\r$//' '{}' \;

# Set system path to BNG2.pl
sed -e 's|../../../source/BioNetGen/BNG2.pl|%{perl_vendorlib}/BioNetGen/BNG2.pl|g' -i examples/S95_regression/lrmsim.txt \
 examples/S12_bionetgen/lrm/lrmsim.txt \
 examples/S12_bionetgen/abba/abbasim.txt \
 examples/S94_archive/Andrews_2016/BioNetGen/lrm/lrmsim.txt \
 examples/S94_archive/Andrews_2016/BioNetGen/abba/abbasim.txt
 
# Copy license file
cp -p source/libSteve/SFMT/LICENSE.txt source/libSteve/SFMT/SFMT-LICENSE.txt
cp -p source/libSteve/SFMT/README.txt source/libSteve/SFMT/SFMT-README.txt

# Remove Python byte cache from previous Python versions shipped in upstream tarball
find -name '*.pyc' -delete

%build

%cmake -Wno-dev \
%if "%{?_lib}" == "lib64"
 %{?_cmake_lib_suffix64} \
%endif
 -DCPACK_BINARY_STGZ:BOOL=OFF \
 -DCPACK_BINARY_TGZ:BOOL=OFF \
 -DCPACK_BINARY_TZ:BOOL=OFF \
 -DCPACK_SOURCE_TBZ2:BOOL=OFF \
 -DCPACK_SOURCE_TGZ:BOOL=OFF \
 -DCPACK_SOURCE_TXZ:BOOL=OFF \
 -DCPACK_SOURCE_TZ:BOOL=OFF \
 -DOPTION_VCELL:BOOL=OFF \
%if %{?with_vtk}
 -DOPTION_VTK:BOOL=ON \
%else
 -DOPTION_VTK:BOOL=OFF \
%endif
 -DBUILD_SHARED_LIBS:BOOL=ON \
 -DSMOLDYN_VERSION:STRING=%{version} \
 -DSMOLDYN_VERSION_MAJOR:STRING=2 \
 -DOPTION_TARGET_LIBSMOLDYN:BOOL=ON \
 -DOPTION_STATIC:BOOL=OFF \
 -DOPTION_PYTHON:BOOL=ON -DPYBIND11_FINDPYTHON:BOOL=ON -Dpybind11_DIR:PATH=%{_datadir}/cmake/pybind11 \
 -DOPTION_USE_ZLIB:BOOL=ON \
 -DOPTION_PDE:BOOL=ON \
 -DPERL_VENDORLIB:PATH=%{perl_vendorlib} \
 -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DLIB_INSTALL_DIR:PATH=%{_libdir} \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DHAVE_GL_FREEGLUT_H=TRUE -DOPTION_EXAMPLES:BOOL=OFF -DOPTION_DOCS:BOOL=OFF
%cmake_build
%install
%cmake_install
pushd %{__cmake_builddir}/py
mkdir -p %{buildroot}%{python3_sitearch}
cp -a smoldyn *.egg-info %{buildroot}%{python3_sitearch}/
popd
%oreon_autofiles python3-smoldyn usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd %{__cmake_builddir}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export PYTHONPATH=%{buildroot}%{python3_sitearch}
xvfb-run ctest -j1 -R "test_api|test_sanity|test_biosimulator" --output-on-failure
popd
%files -f %{oreon_filedir}/main.list
%files -n smoldyn-doc -f %{oreon_filedir}/smoldyn-doc.list
%files -n smoldyn-libs -f %{oreon_filedir}/smoldyn-libs.list
%files -n smoldyn-libs-devel -f %{oreon_filedir}/smoldyn-libs-devel.list
%files -n python3-smoldyn -f %{oreon_filedir}/python3-smoldyn.list

%changelog

%autochangelog
