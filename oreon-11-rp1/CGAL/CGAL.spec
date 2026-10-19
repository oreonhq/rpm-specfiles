%global source0_hash b6be77c60765a8456335de991eeaf6ffec55256984e4a9ecc6a97c37bbfe85bf
%global debug_package %{nil}
%global boost_version 1.74
%global qt_version 6.4
%global cmake_version 3.22
%global fullversion %{version}
Name:           CGAL
Version:        6.2.1
Release:        1%{?dist}
Summary:        Computational Geometry Algorithms Library
License:        LGPL-3.0-or-later AND GPL-3.0-or-later AND BSL-1.0
URL:            http://www.cgal.org/
Source0:        https://github.com/%{name}/cgal/releases/download/v%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
Libraries for CGAL applications.
CGAL is a collaborative effort of several sites in Europe and
Israel. The goal is to make the most important of the solutions and
methods developed in computational geometry available to users in
industry and academia in a C++ library. The goal is to provide easy
access to useful, reliable geometric algorithms.

%package devel
Summary:        Development files and tools for CGAL applications
Provides:       CGAL-static = %{version}-%{release}
Requires:       cmake
Requires:       boost-devel%{?_isa} >= %{boost_version}
Requires:       gmp-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}
Recommends:     zlib-devel%{?_isa}
Recommends:     eigen3-devel
%description devel
Libraries for CGAL applications.
CGAL is a collaborative effort of several sites in Europe and
Israel. The goal is to make the most important of the solutions and
methods developed in computational geometry available to users in
industry and academia in a C++ library. The goal is to provide easy
access to useful, reliable geometric algorithms.
The %{name}-devel package provides the headers files and tools you may need to
develop applications using CGAL.

%package qt6-devel
Summary:        Development files and tools for CGAL applications using CGAL_qt6
Requires:       %{name}-devel = %{version}-%{release}
Requires:       qt6-qtbase-devel%{?_isa} >= %{qt_version}
Requires:       qt6-qtsvg-devel%{?_isa} >= %{qt_version}
Requires:       qt6-qtdeclarative-devel%{?_isa} >= %{qt_version}
Requires:       qt6-qttools-devel%{?_isa} >= %{qt_version}
%description qt6-devel
The %{name}-qt6-devel package provides the headers files and tools you
may need to develop applications using the CGAL_qt6 component of CGAL.

%package demos-source
BuildArch:      noarch
Summary:        Examples and demos of CGAL algorithms
Requires:       %{name}-devel = %{version}-%{release}
%description demos-source
The %{name}-demos-source package provides the sources of examples and demos of
CGAL algorithms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{fullversion}

# Fix some file permissions
#chmod a-x include/CGAL/export/ImageIO.h

# Install README.Fedora here, to include it in %%doc
cat << 'EOF' > ./README.Fedora
Header-only
-----------
CGAL is a header-only library since version 5.0.

Packages
--------
In Fedora, the CGAL tarball is separated in several packages:
  - CGAL is empty since CGAL-5.0
  - CGAL-devel contains header files, and several files and tools needed to
  develop CGAL applications,
  - CGAL-demos-source contains the source of examples and demos of CGAL.

Documentation
-------------
Note that the CGAL documentation cannot be packaged for Fedora due to unclear
license conditions. The complete documentation in PDF and HTML is
available at http://www.cgal.org/Manual/index.html
EOF

%build

%cmake -DCGAL_DO_NOT_WARN_ABOUT_CMAKE_BUILD_TYPE=ON -DCGAL_INSTALL_LIB_DIR=%{_datadir} -DCGAL_INSTALL_DOC_DIR=
%cmake_build
%install
rm -rf %{buildroot}
%cmake_install
mkdir -p %{buildroot}%{_datadir}/CGAL
touch -r demo %{buildroot}%{_datadir}/CGAL/
cp -a demo %{buildroot}%{_datadir}/CGAL/demo
cp -a examples %{buildroot}%{_datadir}/CGAL/examples
%oreon_autofiles CGAL-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles CGAL-qt6-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles CGAL-demos-source usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm -rf include/
mkdir build-example
cd build-example
cmake -L "-DCMAKE_PREFIX_PATH=%{buildroot}/usr" %{buildroot}%{_datadir}/CGAL/examples/Triangulation_2
make constrained_plus
ldd ./constrained_plus
./constrained_plus
%files -f %{oreon_filedir}/main.list
%files -n CGAL-devel -f %{oreon_filedir}/CGAL-devel.list
%files -n CGAL-qt6-devel -f %{oreon_filedir}/CGAL-qt6-devel.list
%files -n CGAL-demos-source -f %{oreon_filedir}/CGAL-demos-source.list

%changelog

%autochangelog
