%global source0_hash 2ad217c56afd2e2560b2f26d01a3bf465dbb88bf488d67f2cbdfe382e6df517a
Name:    libefp
Version: 1.5.0
Release:        22%{?dist}
Summary:        A full implementation of the Effective Fragment Potential (EFP) method
License: LicenseRef-Callaway-BSD 
URL:     https://libefp.github.io/
Source0:        https://github.com/ilyak/libefp/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: libefp-1.5.0-destdir.patch
Patch1: libefp-1.5.0-shared.patch
Requires: %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-gfortran
BuildRequires:  make
# /oreon:deps
%description
The Effective Fragment Potential (EFP) method allows one to describe
large molecular systems by replacing chemically inert part of a system
by a set of Effective Fragments while performing regular ab initio
calculation on the chemically active part. The LIBEFP library is a
full implementation of the EFP method. It allows users to easily
incorporate EFP support into their favourite quantum chemistry
package.

%package data
Summary:  Data files for libefp
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description data
This package provides the data files needed by libefp.

%package devel
Summary:  Development headers for libefp
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the development headers for libefp.

%package -n efpmd
Summary: A molecular simulation program based on LIBEFP
%description -n efpmd
EFPMD is a molecular simulation program based on LIBEFP. It supports
single point energy and gradient calculations, semi-numerical Hessian
and normal mode analysis, geometry optimization, molecular dynamics
simulations in microcanonical (NVE), canonical (NVT), and
isobaric-isothermal (NPT) ensembles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .destdir
%patch -P1 -p1 -b .sharedlib
cat > config.inc <<EOF
# C compiler
CC= gcc
# Fortran compiler
FC= gfortran
# install prefix
PREFIX=%{_prefix}
# fragment library path
FRAGLIB=%{_prefix}/share/libefp/fraglib
# additional link libraries
MYLIBS=-lflexiblas -lgfortran
# additional linker flags
MYLDFLAGS=
# additional C flags
MYCFLAGS=%{optflags} -std=c99 -fopenmp -fPIC
# additional Fortran flags
MYFFLAGS=%{optflags} -fPIC
EOF

%build

make %{?_smp_mflags}
%install
%make_install LIBDIR=%{_libdir}
\rm %{buildroot}%{_bindir}/cubegen.pl
\rm %{buildroot}%{_bindir}/trajectory.pl
\rm %{buildroot}%{_libdir}/libefp.so
libname=$(ls %{buildroot}%{_libdir}/libefp.so.*)
ln -s $(basename $libname) %{buildroot}%{_libdir}/libefp.so
%oreon_autofiles efpmd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=$(pwd)/src
make check
%files -f %{oreon_filedir}/main.list
%files -n libefp-data -f %{oreon_filedir}/libefp-data.list
%files -n libefp-devel -f %{oreon_filedir}/libefp-devel.list
%files -n efpmd -f %{oreon_filedir}/efpmd.list

%changelog

%autochangelog
