%global source0_hash c517ce61820ea8114664a4280b6a6bc74a4f22f1fd1ea4ddecd6df0caeeae4f4
%ifarch %{arm} %{ix86} s390x
%global _lto_cflags %nil
%endif
%ifarch %{arm} %{ix86}
%global lxcflag -DDISABLE_LXC=ON
%else
%global lxcflag -DDISABLE_LXC=OFF
%endif
%global soversion 15
Name:           libxc
Summary:        Library of exchange and correlation functionals for density-functional theory
Version:        7.1.2
Release:        1%{?dist}
License:        MPL-2.0
Source0:        https://gitlab.com/libxc/libxc/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         libxc-7.0.0-pylibxc.patch
URL:            http://www.tddft.org/programs/octopus/wiki/index.php/Libxc
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
# /oreon:deps
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
%{?python_provide:%python_provide python3-%{name}}
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

export CMAKE_POLICY_VERSION_MINIMUM=3.5
export CFLAGS="%{optflags} -fno-var-tracking-assignments"
%cmake -DDISABLE_VXC=OFF -DDISABLE_FXC=OFF -DDISABLE_KXC=OFF %{lxcflag} -DENABLE_FORTRAN=ON -DENABLE_PYTHON=ON -DENABLE_XHOST=OFF
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/*.mod %{buildroot}%{_fmoddir}
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_libdir}/pylibxc %{buildroot}%{python3_sitearch}
rm -f %{buildroot}%{_includedir}/libxc.bib
sed -i 's|${_IMPORT_PREFIX}/include/|%{_libdir}/gfortran/modules|g' %{buildroot}%{_libdir}/cmake/Libxc/LibxcTargets-Fortran.cmake
sed -i 's|includedir=${prefix}/include/|includedir=%{_libdir}/gfortran/modules|g' %{buildroot}%{_libdir}/pkgconfig/libxcf03.pc
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest --parallel 1
%files -f %{oreon_filedir}/main.list
%files -n libxc-devel -f %{oreon_filedir}/libxc-devel.list
%files -n python3-libxc -f %{oreon_filedir}/python3-libxc.list

%changelog

%autochangelog
