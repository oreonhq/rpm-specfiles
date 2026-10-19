%global source0_hash 1456cac5cd67353e19e1c6e57546af052a9302b7fbe2deaa649a44eec45fbec8
%global major_soversion 2
%global minor_soversion 8
Name:           stellarsolver
Version:        2.8
Release:        1%{?dist}
Summary:        The Cross Platform Sextractor and Internal Astrometric Solver
License:        BSD-3-Clause and GPL-2.0-or-later and GPL-3.0-or-later and LGPL-2.0-or-later and LGPL-3.0-or-later and MIT
URL:            https://github.com/rlancaste/%{name}/
Source0:        https://github.com/rlancaste/%{name}//archive/%{version}/%{name}-%{version}.tar.gz
Provides:       bundled(astrometry) = 0.89
Provides:       bundled(sep) = 1.2.0
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cfitsio-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  wcslib-devel
# /oreon:deps
%description
StellarSolver is the Cross Platform Sextractor and Internal Astrometric Solver:
* An Astrometric Plate Solver for Mac, Linux, and Windows, built on
  Astrometry.net and SEP (sextractor)
* Meant to be an internal library for use in a program like KStars for internal
  plate solving on all supported operating systems

%package        libs
Summary:        Shared library of StellarSolver
%description    libs
Shared library of Stellarsolver, meant to be an internal library for use in
a program like KStars for internal plate solving on all supported operating
systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

%forgeautosetup -p1

%build

%cmake -DBUILD_TESTER=ON \
       -DBUILD_BATCH_SOLVER=ON \
       -DUSE_QT5=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/com.github.rlancaste.%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.github.rlancaste.stellarbatchsolver.desktop
%files -f %{oreon_filedir}/main.list
%files -n stellarsolver-libs -f %{oreon_filedir}/stellarsolver-libs.list
%files -n stellarsolver-devel -f %{oreon_filedir}/stellarsolver-devel.list

%changelog

%autochangelog
