%global source0_hash none

# Turn off LTO for architectures where this fails
%ifarch %{arm} %{ix86} s390x
%global _lto_cflags %nil
%endif

# Turn off 4th derivatives for 32-bit targets
%ifarch %{arm} %{ix86}
%global lxcflag -DDISABLE_LXC=ON
%else
%global lxcflag -DDISABLE_LXC=OFF
%endif

# Shared library version
%global soversion 15

Name:           libxc
Summary:        Library of exchange and correlation functionals for density-functional theory
Version:        7.0.0
Release:        10%{?dist}
License:        MPL-2.0
Source0:        https://gitlab.com/libxc/libxc/-/archive/%{version}/%{name}-%{version}.tar.gz
# Don't rebuild libxc for pylibxc
Patch0:         libxc-7.0.0-pylibxc.patch
URL:            http://www.tddft.org/programs/octopus/wiki/index.php/Libxc

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools

%description
libxc is a library of exchange and correlation functionals. Its purpose is to
be used in codes that implement density-functional theory. For the moment, the
library includes most of the local density approximations (LDAs), generalized
density approximation (GGAs), and meta-GGAs. The library provides values for
the energy density and its 1st, 2nd, 3rd, and 4th derivatives.

%package devel
Summary:        Development library and headers for libxc
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake

%description devel
libxc is a library of exchange and correlation functionals. Its purpose is to
be used in codes that implement density-functional theory. For the moment, the
library includes most of the local density approximations (LDAs), generalized
density approximation (GGAs), and meta-GGAs. The library provides values for
the energy density and its 1st, 2nd, 3rd, and 4th derivatives.

This package contains the development headers and library that are necessary
in order to compile programs against libxc.

%package -n python3-%{name}
Summary:        Python3 interface to libxc
Requires:       python3-numpy
Requires:       %{name} = %{version}-%{release}
Obsoletes:      python2-%{name} < %{version}-%{release}
Obsoletes:      python3-%{name} < %{version}-%{release}
%if 0%{?rhel}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
%else
%{?python_provide:%python_provide python3-%{name}}
%endif
%description -n python3-%{name}
libxc is a library of exchange and correlation functionals. Its purpose is to
be used in codes that implement density-functional theory. For the moment, the
library includes most of the local density approximations (LDAs), generalized
density approximation (GGAs), and meta-GGAs. The library provides values for
the energy density and its 1st, 2nd, 3rd, and 4th derivatives.

This package contains the Python3 interface library to libxc.

%prep
%setup -q
%patch 0 -p1 -b .pylibxc
# Plug in library soversion
sed -i "s|@SOVERSION@|%{soversion}|g;s|@LIBDIR@|%{_libdir}|g" pylibxc/core.py

%build
# TODO: Please submit an issue to upstream (rhbz#2380769)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# Disable var tracking assignments for C sources, since it fails anyhow due to the size of the sources
export CFLAGS="%{optflags} -fno-var-tracking-assignments"
%cmake -DDISABLE_VXC=OFF -DDISABLE_FXC=OFF -DDISABLE_KXC=OFF %{lxcflag} -DENABLE_FORTRAN=ON -DENABLE_PYTHON=ON -DENABLE_XHOST=OFF
%cmake_build

%install
%cmake_install
# Move modules in the right place
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/*.mod %{buildroot}%{_fmoddir}
# Move python library to the right place
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_libdir}/pylibxc %{buildroot}%{python3_sitearch}

# Remove bibtex bibliography placed in an odd location
rm -f %{buildroot}%{_includedir}/libxc.bib

# Patch the location of the moved files (BZ #2365328)
sed -i 's|${_IMPORT_PREFIX}/include/|%{_libdir}/gfortran/modules|g' %{buildroot}%{_libdir}/cmake/Libxc/LibxcTargets-Fortran.cmake
sed -i 's|includedir=${prefix}/include/|includedir=%{_libdir}/gfortran/modules|g' %{buildroot}%{_libdir}/pkgconfig/libxcf03.pc

%ldconfig_scriptlets

# Run tests, don't parallellize them
%check
%ctest --parallel 1

%files
%doc README NEWS AUTHORS ChangeLog.md libxc.bib
%license COPYING
%{_bindir}/xc-info
%{_libdir}/libxc.so.%{soversion}*
%{_libdir}/libxcf03.so.%{soversion}*

%files devel
%{_libdir}/libxc.so
%{_libdir}/libxcf03.so
%{_includedir}/xc*.h
%{_fmoddir}/xc_f03_*.mod
%{_libdir}/pkgconfig/libxc.pc
%{_libdir}/pkgconfig/libxcf03.pc
%{_libdir}/cmake/Libxc/

%files -n python3-%{name}
%{python3_sitearch}/pylibxc/

%changelog
%autochangelog
