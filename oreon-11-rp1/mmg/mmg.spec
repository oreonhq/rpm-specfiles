%global source0_hash 686eaab84de79c072f3aedf26cd11ced44c84b435d51ce34e016ad203172922f
Name:           mmg
Version:        5.8.0
Release:        1%{?dist}
Summary:        Surface and volume remeshers
License:        LGPL-3.0-or-later
URL:            https://www.mmgtools.org/
Source0:        https://github.com/MmgTools/mmg/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         mmg_doc.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  scotch-devel
# /oreon:deps
%description
mmg is an open source software for bidimensional and tridimensional surface and
volume remeshing. It provides:
- The mmg2d application and library: adaptation and optimization of a
  bidimensional triangulation
- The mmgs application and library: adaptation and optimization of a surface
  triangulation and isovalue discretization
- The mmg3d application and library: adaptation and optimization of a
  tetrahedral mesh and implicit domain meshing
- The mmg library, combining the mmg2d, mmgs and mmg3d libraries.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Development documentation for mmg
Obsoletes:      mmgs-devel-doc < 5.7.0
Provides:       mmgs-devel-doc = %{version}-%{release}
Obsoletes:      mmg2d-devel-doc < 5.7.0
Provides:       mmg2d-devel-doc = %{version}-%{release}
Obsoletes:      mmg3d-devel-doc < 5.7.0
Provides:       mmg3d-devel-doc = %{version}-%{release}
BuildArch:      noarch
%description doc
This package contains the documentation for developing
applications that use mmg.

###############################################################################

%package -n mmgs
Summary:        Surface remesher
%description -n mmgs
The mmgs application and library: adaptation and optimization of a surface
triangulation and isovalue discretization.

%package -n mmgs-devel
Summary:        Development files for mmgs
Requires:       mmgs%{?_isa} = %{version}-%{release}
Requires:       mmg-devel%{?_isa} = %{version}-%{release}
%description -n mmgs-devel
The mmgs-devel package contains libraries and header files for
developing applications that use mmgs.

###############################################################################

%package -n mmg2d
Summary:        Surface remesher
%description -n mmg2d
The mmg2d application and library: adaptation and optimization of a
bidimensional triangulation.

%package -n mmg2d-devel
Summary:        Development files for mmg2d
Requires:       mmg2d%{?_isa} = %{version}-%{release}
Requires:       mmg-devel%{?_isa} = %{version}-%{release}
%description -n mmg2d-devel
The mmg2d-devel package contains libraries and header files for
developing applications that use mmg2d.

###############################################################################

%package -n mmg3d
Summary:        Volume remesher
Obsoletes:      mmg3d-libs < 5.3.10
Provides:       mmg3d-libs = %{version}-%{release}
%description -n mmg3d
The mmg3d application and library: adaptation and optimization of a
tetrahedral mesh and implicit domain meshing.

%package -n mmg3d-devel
Summary:        Development files for mmg3d
Requires:       mmg3d%{?_isa} = %{version}-%{release}
Requires:       mmg-devel%{?_isa} = %{version}-%{release}
%description -n mmg3d-devel
The mmg3d-devel package contains libraries and header files for
developing applications that use mmg3d

###############################################################################

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_SHARED_LIBS=ON -DBUILD_DOC=ON
%cmake_build
%cmake_build -- doc
%install
%cmake_install
ln -s mmg2d_O3 %{buildroot}/%{_bindir}/mmg2d
ln -s mmgs_O3 %{buildroot}/%{_bindir}/mmgs
ln -s mmg3d_O3 %{buildroot}/%{_bindir}/mmg3d
install -Dpm 0644 doc/man/mmg2d.1.gz %{buildroot}%{_mandir}/man1/mmg2d.1.gz
install -Dpm 0644 doc/man/mmgs.1.gz %{buildroot}%{_mandir}/man1/mmgs.1.gz
install -Dpm 0644 doc/man/mmg3d.1.gz %{buildroot}%{_mandir}/man1/mmg3d.1.gz
%oreon_autofiles mmgs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mmgs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles mmg2d usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mmg2d-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles mmg3d usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mmg3d-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mmg-devel -f %{oreon_filedir}/mmg-devel.list
%files -n mmg-doc -f %{oreon_filedir}/mmg-doc.list
%files -n mmgs -f %{oreon_filedir}/mmgs.list
%files -n mmgs-devel -f %{oreon_filedir}/mmgs-devel.list
%files -n mmg2d -f %{oreon_filedir}/mmg2d.list
%files -n mmg2d-devel -f %{oreon_filedir}/mmg2d-devel.list
%files -n mmg3d -f %{oreon_filedir}/mmg3d.list
%files -n mmg3d-devel -f %{oreon_filedir}/mmg3d-devel.list

%changelog

%autochangelog
