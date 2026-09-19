%global source0_hash 40b9c03df57d73412d75ee4098937706d95e252b4f40d091cc13633a0c56d20e

# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

Name:           permlib
Version:        0.2.9
Release:        26%{?dist}
Summary:        Library for permutation computations

License:        BSD-3-Clause
URL:            https://github.com/tremlin/PermLib
VCS:            git:%{url}.git
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Doxygen config file written by Jerry James <loganjerry@gmail.com>
Source1:        %{name}-Doxyfile
# Fix gcc 6 build failure
Patch:          %{name}-0.2.8-gcc6.patch
# Adapt to changes in recent versions of boost
Patch:          %{name}-0.2.9-boost.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dvipng
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  tex(newunicodechar.sty)

%description
PermLib is a callable C++ library for permutation computations.  Currently it
supports set stabilizer and in-orbit computations, based on bases and strong
generating sets (BSGS).  Additionally, it computes automorphisms of symmetric
matrices and finds the lexicographically smallest set in an orbit of sets.

%package devel
# The code is BSD-3-Clause.  Other licenses are due to files added by doxygen.
# GPL-1.0-or-later: html/*.{css,png,svg}
# MIT: html/*.js
License:        BSD-3-Clause AND GPL-1.0-or-later AND MIT
Summary:        Header files for developing programs that use PermLib
BuildArch:      noarch
Requires:       boost-devel
Provides:       %{name}-static = %{version}-%{release}
Provides:       bundled(js-jquery)

%description devel
PermLib is a callable C++ library for permutation computations.  Currently it
supports set stabilizer and in-orbit computations, based on bases and strong
generating sets (BSGS).  Additionally, it computes automorphisms of symmetric
matrices and finds the lexicographically smallest set in an orbit of sets.

This package contains header files for developing programs that use
PermLib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n PermLib-%{version}
sed "s/@VERSION@/%{version}/" %{SOURCE1} > Doxyfile

# Remove flags that break the build with boost 1.90.0
sed -i 's/ -ansi -pedantic//' CMakeLists.txt

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

# Build the documentation
mkdir doc
doxygen
rm -f doc/html/installdox

%install
# No install target is generated in the makefile, and
# DESTDIR=$RPM_BUILD_ROOT cmake -P cmake_install.cmake
# does nothing, so we do it by hand.

# Install the header files
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a include/%{name} $RPM_BUILD_ROOT%{_includedir}

%check
%ctest

%files devel
%doc AUTHORS CHANGELOG doc/html
%license LICENSE
%{_includedir}/permlib

%changelog
%autochangelog
