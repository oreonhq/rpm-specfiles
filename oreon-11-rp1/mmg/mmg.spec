%global source0_hash 686eaab84de79c072f3aedf26cd11ced44c84b435d51ce34e016ad203172922f

Name:           mmg
Version:        5.8.0
Release:        4%{?dist}
Summary:        Surface and volume remeshers

License:        LGPL-3.0-or-later
URL:            https://www.mmgtools.org/
Source0:        https://github.com/MmgTools/mmg/archive/v%{version}/%{name}-%{version}.tar.gz

# Don't generate latex doc output, place html output to subdir
Patch0:         mmg_doc.patch

BuildRequires:  doxygen
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  scotch-devel

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

%autosetup -p1

%build
%cmake -DBUILD_SHARED_LIBS=ON -DBUILD_DOC=ON
%cmake_build
%cmake_build -- doc

%install
%cmake_install

# Install suffix-less symlinks
ln -s mmg2d_O3 %{buildroot}/%{_bindir}/mmg2d
ln -s mmgs_O3 %{buildroot}/%{_bindir}/mmgs
ln -s mmg3d_O3 %{buildroot}/%{_bindir}/mmg3d

# Install man pages
install -Dpm 0644 doc/man/mmg2d.1.gz %{buildroot}%{_mandir}/man1/mmg2d.1.gz
install -Dpm 0644 doc/man/mmgs.1.gz %{buildroot}%{_mandir}/man1/mmgs.1.gz
install -Dpm 0644 doc/man/mmg3d.1.gz %{buildroot}%{_mandir}/man1/mmg3d.1.gz

%files
%doc AUTHORS README.md
%license LICENSE COPYING COPYING.LESSER
%{_libdir}/libmmg.so.*

%files devel
%dir %{_includedir}/mmg
%{_includedir}/mmg/common/
%{_includedir}/mmg/libmmg.h
%{_includedir}/mmg/libmmgf.h
%{_libdir}/libmmg.so
%{_libdir}/cmake/mmg/

%files doc
%doc %{__cmake_builddir}/doc/html

%files -n mmg2d
%doc AUTHORS README.md
%license LICENSE COPYING COPYING.LESSER
%{_bindir}/mmg2d_O3
%{_bindir}/mmg2d
%{_libdir}/libmmg2d.so.*
%{_mandir}/man1/mmg2d.1*

%files -n mmg2d-devel
%dir %{_includedir}/mmg
%{_includedir}/mmg/mmg2d/
%{_libdir}/libmmg2d.so

%files -n mmgs
%doc AUTHORS README.md
%license LICENSE COPYING COPYING.LESSER
%{_bindir}/mmgs_O3
%{_bindir}/mmgs
%{_libdir}/libmmgs.so.*
%{_mandir}/man1/mmgs.1*

%files -n mmgs-devel
%dir %{_includedir}/mmg
%{_includedir}/mmg/mmgs/
%{_libdir}/libmmgs.so

%files -n mmg3d
%doc AUTHORS README.md
%license LICENSE COPYING COPYING.LESSER
%{_bindir}/mmg3d_O3
%{_bindir}/mmg3d
%{_libdir}/libmmg3d.so.*
%{_mandir}/man1/mmg3d.1*

%files -n mmg3d-devel
%dir %{_includedir}/mmg
%{_includedir}/mmg/mmg3d/
%{_libdir}/libmmg3d.so

%changelog
%autochangelog
