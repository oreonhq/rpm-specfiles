%global source0_hash 500db9c3b2617e1f03d0e548977aec10d36811ba1c43bb5ef250c0e3853ae1c2

Name: blitz
Version: 1.0.2
Release: 24%{?dist}
Summary: C++ class library for matrix scientific computing

License: LGPL-3.0-only OR BSD-3-Clause OR Artistic-2.0

URL: https://github.com/blitzpp/blitz
Source0: https://github.com/blitzpp/blitz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Modifications of the Fedora package are listed here:
# * Arch dependent header moved to lib/blitz/include
#   https://sourceforge.net/tracker/?func=detail&aid=3534421&group_id=63961&atid=505791
Source1: README.fedora
Patch0: blitz-cmake-path.patch

BuildRequires: gcc-c++
BuildRequires: gcc-gfortran doxygen texinfo graphviz
BuildRequires: cmake
BuildRequires: python3 texinfo-tex
BuildRequires: make

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

# blitz.pc is created directly by configure
# I use sed to add %%libdir/blitz to the include directories of the library
# so that different bzconfig.h can be installed for different archs
# 
# The problem is reported here
# https://sourceforge.net/tracker/?func=detail&aid=2273091&group_id=63961&atid=505791
#%{__sed} -i -e "s/Cflags: -I\${includedir}/Cflags: -I\${includedir} -I\${libdir}\/blitz\/include/" blitz.pc

%install
%cmake_install

#mkdir -p %{buildroot}%{_libdir}/blitz/include/blitz
#mv %{buildroot}%{_includedir}/blitz/gnu %{buildroot}%{_libdir}/blitz/include/blitz

# Put in doc only the source code
rm -rf examples/.deps
rm -rf examples/Makefile*

%check
ctest -V %{?_smp_mflags}

%files
%doc AUTHORS README.md README.fedora
%license LEGAL COPYING COPYING.LESSER LICENSE
%{_libdir}/libblitz.so.*

%files devel
%doc examples
%{_libdir}/pkgconfig/*
%{_includedir}/blitz
%{_includedir}/random
%{_libdir}/cmake/*
%{_libdir}/libblitz.so
%exclude %{_libdir}/libblitz.a

%files doc
%doc AUTHORS README.md README.fedora
%license COPYING COPYING.LESSER LICENSE

%changelog
%autochangelog
