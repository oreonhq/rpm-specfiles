%global source0_hash 500db9c3b2617e1f03d0e548977aec10d36811ba1c43bb5ef250c0e3853ae1c2
Name: blitz
Version: 1.0.2
Release:        24%{?dist}
Summary:        C++ class library for matrix scientific computing
License: LGPL-3.0-only OR BSD-3-Clause OR Artistic-2.0
URL: https://github.com/blitzpp/blitz
Source0:        https://github.com/blitzpp/blitz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: README.fedora
Patch0: blitz-cmake-path.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# /oreon:deps
%description
Blitz++ is a C++ class library for scientific computing which provides 
performance on par with Fortran 77/90. It uses template techniques to achieve 
high performance. Blitz++ provides dense arrays and vectors, random number 
generators, and small vectors

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files and libraries needed to develop a %{name}
application

%package doc
Summary: The Blitz html docs
BuildArch: noarch
%description doc
HTML documentation files for the Blitz Library

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
cp %SOURCE1 .

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
rm -rf examples/.deps
rm -rf examples/Makefile*
%oreon_autofiles blitz-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles blitz-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

ctest -V %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list
%files -n blitz-devel -f %{oreon_filedir}/blitz-devel.list
%files -n blitz-doc -f %{oreon_filedir}/blitz-doc.list

%changelog

%autochangelog
