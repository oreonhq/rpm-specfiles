%global source0_hash ce573bbea8e75b429f8c3d3e86498741ba3dc9628a1530d2f65268397ad059e8
Name: cfitsio
Version: 4.7.0
Release:        1%{?dist}
Summary:        Library for manipulating FITS data files
License: CFITSIO
URL: https://heasarc.gsfc.nasa.gov/fitsio/
Source0:        https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/cfitsio-%{version}.tar.gz
Patch0: cfitsio-noversioncheck.patch
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  curl-devel
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
CFITSIO is a library of C and FORTRAN subroutines for reading and writing 
data files in FITS (Flexible Image Transport System) data format. CFITSIO 
simplifies the task of writing software that deals with FITS files by 
providing an easy to use set of high-level routines that insulate the 
programmer from the internal complexities of the FITS file format. At the 
same time, CFITSIO provides many advanced features that have made it the 
most widely used FITS file programming interface in the astronomical 
community.

%package devel
Summary: Headers required when building programs against cfitsio
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
Headers required when building a program against the cfitsio library.

%package static
Summary: Static cfitsio library
%description static
Static cfitsio library; avoid use if possible.

%package docs
Summary: Documentation for cfitsio
BuildArch:  noarch
%description docs
Stand-alone documentation for cfitsio.

%package utils
Summary: CFITSIO based utilities
Requires: %{name} = %{version}-%{release}
Provides: fpack{?_isa} = %{version}-%{release}
Obsoletes: fpack <= 4.5.0-1  
Provides: fitsverify{?_isa} = 4.22-5
Obsoletes: fitsverify <= 4.22-4
%description utils
This package contains utility programas provided by CFITSIO

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --enable-reentrant --with-bzip2 --includedir=%{_includedir}/%{name}
make %{?_smp_mflags}
%check

make testprog
LD_LIBRARY_PATH=. ./testprog > testprog.lis
cmp -s testprog.lis testprog.out
cmp -s testprog.fit testprog.std
%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/%{_bindir}/cookbook
rm %{buildroot}/%{_bindir}/smem
rm %{buildroot}/%{_bindir}/speed
%ldconfig_scriptlets
%oreon_autofiles cfitsio-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cfitsio-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cfitsio-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cfitsio-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n cfitsio-devel -f %{oreon_filedir}/cfitsio-devel.list
%files -n cfitsio-static -f %{oreon_filedir}/cfitsio-static.list
%files -n cfitsio-docs -f %{oreon_filedir}/cfitsio-docs.list
%files -n cfitsio-utils -f %{oreon_filedir}/cfitsio-utils.list

%changelog

%autochangelog
