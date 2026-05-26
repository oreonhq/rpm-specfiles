# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 8774e9a12c70b0180b95d6b0b563c5aa4bea8d5960c15e18ae3b6d2521d64f8b
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary: General dimension convex hull programs
Name: qhull
Version: 8.0.2
# Add epoch, because upstream changed their versioning scheme:
# - Older releases used year.month
# - Newer releases use x.y.z
Epoch: 1
Release: 8%{?dist}
License: Qhull
Source0: https://github.com/qhull/qhull/archive/v%{version}.tar.gz#/qhull-%{version}.tar.gz

# Install cmake and pkgconfig file into proper libdir
# https://github.com/qhull/qhull/pull/123
Patch0: qhull-lib64.patch
# Install extra targets - libqhull and qhull_p
Patch1: qhull-install.patch
# The static_r library needs fPIC
Patch2: qhull-staticr-pic.patch

URL: http://www.qhull.org

BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: chrpath

%description
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

%package -n libqhull
Summary: -n libqhull

%description -n libqhull
%{summary}

%package -n libqhull_r
Summary: libqhull_r

%description -n libqhull_r
%{summary}

%package -n libqhull_p
Summary: libqhull_p

%description -n libqhull_p
%{summary}

%package devel
Summary: Development files for qhull
Requires: lib%{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: lib%{name}_r%{?_isa} = %{epoch}:%{version}-%{release}
Requires: lib%{name}_p%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

%prep
%oreon_verify_sources
%setup -q
%patch -P0 -p1 -b .lib64
%patch -P1 -p1 -b .install
%patch -P2 -p1 -b .pic

%build
mkdir -p build
cd build
%cmake -S .. -B . -DLINK_APPS_SHARED=ON
make VERBOSE=1 %{?_smp_mflags}
# These items are deprecated as of 8.0.2
make VERBOSE=1 %{?_smp_mflags} libqhull qhull_p
cd ..

%install
cd build
make VERBOSE=1 DESTDIR=$RPM_BUILD_ROOT install
cd ..

chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/lib*.so.*


%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/COPYING.txt
%license COPYING.txt
%{_bindir}/*
%{_mandir}/man1/*

%files -n libqhull
%{_libdir}/libqhull.so.*

%ldconfig_scriptlets -n libqhull


%files -n libqhull_r
%{_libdir}/libqhull_r.so.*

%ldconfig_scriptlets -n libqhull_r


%files -n libqhull_p
%{_libdir}/libqhull_p.so.*

%ldconfig_scriptlets -n libqhull_p


%files devel
%{_libdir}/*.so
%{_includedir}/*
# Easier to include these than to hack them out of the cmake bits
%{_libdir}/libqhullcpp.a
%{_libdir}/libqhullstatic*.a
%dir %{_libdir}/cmake/Qhull
%{_libdir}/cmake/Qhull/QhullConfig*.cmake
%{_libdir}/cmake/Qhull/QhullTargets*.cmake
%{_libdir}/pkgconfig/qhull_r.pc
%{_libdir}/pkgconfig/qhullcpp.pc
%{_libdir}/pkgconfig/qhullstatic*.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:8.0.2-8
- Import
