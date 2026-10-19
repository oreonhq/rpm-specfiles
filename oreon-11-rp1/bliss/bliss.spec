%global source0_hash 0acb23352184cbd0c06c361032743de0bff813b6e2460f102dc03c1e9d1a0907
%global giturl  https://github.com/scipopt/Bliss
Name:           bliss
Version:        0.77
Release:        13%{?dist}
Summary:        Compute automorphism groups and canonical labelings of graphs
License:        LGPL-3.0-only
URL:            https://users.aalto.fi/~tjunttil/bliss/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/Bliss-%{version}.tar.gz
Source1:        bliss.1
Patch:          bliss-rehn.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make
# /oreon:deps
%description
Bliss is an open source tool for computing automorphism groups and canonical
forms of graphs.  It has both a command line user interface as well as C++ and
C programming language APIs.

%package devel
License:        LGPL-3.0-only AND MIT AND GPL-1.0-or-later
Summary:        Headers and library files for developing with bliss
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
%description devel
Headers and library files needed to develop applications that use the bliss
library.

%package libs
Summary:        Compute automorphism groups and canonical labelings of graphs
%description libs
A command-line bliss tool to access the functionality of the bliss library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Bliss-%{version} -p0

%conf
# Do not override Fedora build flags.  The last sagemath version added an
# soname.  Duplicate it for compatibility.  Link the library with libgmp.
# Hidden symbols hide ALL symbols, meaning we can't use the library.
sed -e 's/ -O3//' \
    -e '/POSITION_INDEPENDENT/a\ \ VERSION 2.0.0 SOVERSION 2' \
    -e '/^install($/itarget_link_libraries(libbliss ${GMP_LIBRARIES})' \
    -e '/VISIBILITY/d' \
    -i CMakeLists.txt

# Fix installation directories
if [ "%{_lib}" != "lib" ]; then
  sed -i 's,\(DESTINATION \)lib,\1%{_lib},' CMakeLists.txt
fi

%build

%cmake -DUSE_GMP:BOOL=ON
%cmake_build
doxygen
%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
sed 's/@VERSION@/%{version}/' %{SOURCE1} > %{buildroot}%{_mandir}/man1/bliss.1
touch -r %{SOURCE1} %{buildroot}%{_mandir}/man1/bliss.1
%oreon_autofiles bliss-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles bliss-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bliss-devel -f %{oreon_filedir}/bliss-devel.list
%files -n bliss-libs -f %{oreon_filedir}/bliss-libs.list

%changelog

%autochangelog
