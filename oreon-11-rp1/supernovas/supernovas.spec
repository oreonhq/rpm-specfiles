%global source0_hash 18f459b23f80c0e017110d26228ea7ffeba48ed26452f00072c719ec9c4cbc58
%global upstream_version     1.7.2
Name:            supernovas
Version:         1.7.2
Release:        1%{?dist}
Summary:        The Naval Observatory's NOVAS C astronomy library, made better
License:         Unlicense
URL:             https://sigmyne.github.io/SuperNOVAS
Source0:        https://github.com/Sigmyne/SuperNOVAS/archive/refs/tags/v%{version}.tar.gz
ExcludeArch:     %{ix86}
Obsoletes:       %{name}-cio-data < %{version}-%{release} 
Suggests:        %{name}-solsys-calceph = %{version}-%{release}
# oreon:deps
BuildRequires:  calceph-devel(x86-64)
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
# /oreon:deps
%description

SuperNOVAS is a C/C++ astronomy library, providing high-precision astronomical 
calculations such as one might need for running an observatory or a precise 
planetarium program. It is a fork of the Naval Observatory Vector Astrometry 
Software (NOVAS) C version 3.1, providing bug fixes and making it easier to 
use overall.

The main goals of SuperNOVAS are to improve usability, add new features, 
promote best practices, and provide accessible documentation -- all while 
retaining 100 percent API compatibility with NOVAS C 3.1. Thus, if you have 
written code for NOVAS C 3.1, you can build it with SuperNOVAS also.

SuperNOVAS is entirely free to use without licensing restrictions. Its source 
code is compatible with the C90 standard, and hence should be suitable for old 
and new platforms alike. It is light-weight and easy to use, with full support 
for the IAU 2000/2006 standards for sub-micro-arc-second position 
calculations.
 
%package solsys-calceph
Summary: Solar-system plugin based on the CALCEPH C library
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires:        calceph-libs%{?_isa} >= 4.0.0
%description solsys-calceph
Optional SuperNOVAS plugin library that provides Solar-system support via the 
CALCEPH C library. It allows using both JPL (SPK) and INPOP 2.0/3.0 data files 
with SuperNOVAS to obtain precise locations for Solar-system bodies. This 
plugin is currently the preferred option to use for Fedora / RPM Linux 
development, which requires use of precise Solar-system data.

%package devel
Summary:         C development files for the SuperNOVAS C/C++ astronomy library
Requires:        %{name}%{?_isa} = %{version}-%{release}
Requires:        %{name}-solsys-calceph%{?_isa} = %{version}-%{release}
Obsoletes:       %{name}-solsys1 < %{version}-%{release} 
Obsoletes:       %{name}-solsys2 < %{version}-%{release} 
%description devel
This sub-package provides C headers and non-versioned shared library symbolic 
links for the SuperNOVAS C/C++ library. It also provides a default FORTRAN
adapter module (as documentation) that may be used as is, or modified as 
needed, for the the JPL PLEPH module.

%package doc
Summary:         Documentation for the SuperNOVAS C/C++ astronomy library
BuildArch:       noarch
%description doc
This package provides HTML documentation, examples, and legacy adapter 
templates for the SuperNOVAS C/C++ astronomy library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SuperNOVAS-%{upstream_version}

%build

%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_DOC=ON \
    -DENABLE_CALCEPH=ON 
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n supernovas-solsys-calceph -f %{oreon_filedir}/supernovas-solsys-calceph.list
%files -n supernovas-devel -f %{oreon_filedir}/supernovas-devel.list
%files -n supernovas-doc -f %{oreon_filedir}/supernovas-doc.list

%changelog

%autochangelog
