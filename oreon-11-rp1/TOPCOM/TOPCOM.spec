%global source0_hash 4fb10754ee5b76056441fea98f2c8dee5db6f2984d8c14283b49239ad4378ab6
Name:           TOPCOM
Version:        1.1.2
Release:        12%{?dist}
Summary:        Triangulations Of Point Configurations and Oriented Matroids
%global upver %(tr . _ <<< %{version})
License:        GPL-2.0-or-later
URL:            https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/
VCS:            git:%{url}.git
Source0:        https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/%{name}-Downloads/%{name}-%{upver}.tgz
Source1:        %{name}-Makefile
Patch:          %{name}-pessimizing-move.patch
Patch:          %{name}-virtual-destructor.patch
Patch:          %{name}-soplex.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%global topcom_major %(cut -d. -f1 <<< %{version})
%global topcom_minor %(cut -d. -f2 <<< %{version})
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  libsoplex-devel
BuildRequires:  make
BuildRequires:  pkgconfig(cddlib)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(zlib-ng)
BuildRequires:  qsopt-ex-devel
# /oreon:deps
%description
TOPCOM is a package for computing Triangulations Of Point Configurations and
Oriented Matroids.  It was very much inspired by the maple program PUNTOS,
which was written by Jesus de Loera.  TOPCOM is entirely written in C++, so
there is a significant speed up compared to PUNTOS.

%package devel
Summary:        Header files needed to build with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cddlib-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       qsopt-ex-devel%{?_isa}
%description devel
Header files needed to build applications that use the %{name} library.

%package libs
Summary:        Core %{name} functionality in a library
%description libs
Command line tools that expose %{name} library functionality.

%package examples
Summary:        Example inputs and outputs for TOPCOM
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description examples
Example input and output files for TOPCOM.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n topcom-%{version} -p1

%conf
# Fix character encoding
iconv -f iso8859-1 -t utf8 -o README.utf8 README
touch -r README README.utf8
mv -f README.utf8 README

# Mimic upstream's modification of gmpxx.h, using the system gmpxx.h
mkdir -p external/include
sed "s|// \(q\.canonicalize\)|\1|" %{_includedir}/gmpxx.h > \
  external/include/gmpxx.h

%build

sed -e 's|@RPM_OPT_FLAGS@|%{build_cxxflags}|' \
    -e 's|@RPM_LD_FLAGS@|%{build_ldflags}|' \
    -e 's|@bindir@|%{_bindir}|' \
    -e 's|@libdir@|%{_libdir}|' \
    -e 's|@includedir@|%{_includedir}|' \
    -e 's|@version@|%{version}|' \
    -e 's|@major@|%{topcom_major}|' \
    -e 's|@minor@|%{topcom_minor}|' \
    -e 's|#version#|@version@|' \
    %{SOURCE1} > Makefile
%make_build
%install
%make_install
rm -f examples/Makefile*
for bin in cross cube cyclic hypersimplex lattice; do
  mv %{buildroot}%{_bindir}/$bin %{buildroot}%{_bindir}/TOPCOM-$bin
done
rm %{buildroot}%{_bindir}/check
%oreon_autofiles TOPCOM-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles TOPCOM-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles TOPCOM-examples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=$PWD src/check
%files -f %{oreon_filedir}/main.list
%files -n TOPCOM-devel -f %{oreon_filedir}/TOPCOM-devel.list
%files -n TOPCOM-libs -f %{oreon_filedir}/TOPCOM-libs.list
%files -n TOPCOM-examples -f %{oreon_filedir}/TOPCOM-examples.list

%changelog

%autochangelog
