%global source0_hash 9651705c79f77418ef0230aafc0cf1b71b17c1c89e413ee0e5ee7818650ce978
%ifarch %{arm}
%define _lto_cflags %{nil}
%endif
%define _smp_mflags -j4
ExcludeArch: %{ix86}
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global commonflags %(echo %{optflags} | sed "s|-O2||g")
%global optflags %commonflags -O1 -fno-var-tracking-assignments
%global apiversion 1
Name:		libint2
Version:	2.13.1
Release:        1%{?dist}
Summary:        A library for efficient evaluation of electron repulsion integrals
License:	LGPL-3.0-only
URL:		https://github.com/evaleev/libint
Source0:        https://github.com/evaleev/libint/archive/v%{version}.tar.gz
Source1:	libint-%{version}.tar.xz
Source2:	progman-%{version}.pdf
Patch0:         libint-2.8.2-fedoraver.patch
Patch1:         libint-2.9.0-datadir.patch
Provides:	libint2(api)%{?_isa} = %{apiversion}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
# /oreon:deps
%description
LIBINT computes the Coulomb and exchange integrals, which in electronic
structure theory are called electron repulsion integrals (ERIs). This is by
far the most common type of integrals in molecular structure theory.

LIBINT uses recursive schemes that originate in seminal Obara-Saika method and
Head-Gordon and Pople’s variation thereof. The idea of LIBINT is to optimize
computer implementation of such methods by implementing an optimizing compiler
to generate automatically highly-specialized code that runs well on
super-scalar architectures.

%package data
Summary:	Shared data for libint2
Requires:	libint2 = %{version}-%{release}
BuildArch:      noarch
%description data
This package contains shared data for libint2.

%package doc
Summary:	Documentation for libint2
Requires:	libint2 = %{version}-%{release}
BuildArch:      noarch
%description doc
This package contains a programmer's manual and doxygen documentation
for the classes.

%package devel
Summary:	Development headers and libraries for libint2
Requires:	libint2%{?_isa} = %{version}-%{release}
Requires:       cmake
Requires:       boost-devel
Requires:       eigen3-devel
Requires:       gmp-devel
Requires:       mpfr-devel
%description devel
This package contains development headers and libraries for libint2.

%prep

%setup -q -T -b 1 -n libint-%{version}
%patch 0 -p1 -b .fedora
# Copy programmers manual
cp -p %{SOURCE2} doc/progman.pdf

%build

export CXX=g++
%cmake -DENABLE_FORTRAN=ON -DENABLE_MPFR=ON -DLIBINT2_PYTHON=ON -DLIBINT2_INSTALL_LIBDIR=%{_libdir} -DLIBINT2_INSTALL_DATADIR=%{_datadir}/%{name} -DLIBINT2_INSTALL_CMAKEDIR=%{_libdir}/cmake/%{name}
%cmake_build
%install
%cmake_install
find %{buildroot} -name *.la -delete
find %{buildroot} -name *.so* -exec chmod 755 {} \;
mkdir -p %{buildroot}%{macrosdir}
cat > %{buildroot}%{macrosdir}/macros.libint2 << EOF
%_libint2_apiversion %{apiversion}
EOF
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/libint_f.mod %{buildroot}%{_fmoddir}/
%ldconfig_scriptlets
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libint2-data -f %{oreon_filedir}/libint2-data.list
%files -n libint2-doc -f %{oreon_filedir}/libint2-doc.list
%files -n libint2-devel -f %{oreon_filedir}/libint2-devel.list

%changelog

%autochangelog
