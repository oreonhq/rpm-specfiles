%global source0_hash c23f72ab74bbf65599f8c0b599d6336fabe1ec2a09c19b70544eeefdc069b73b

%global snapshot 121130

Name:           gts
Version:        0.7.6
Release:        52.20%{snapshot}%{?dist}
Summary:        GNU Triangulated Surface Library
License:        LGPL-2.0-or-later
URL:            http://gts.sourceforge.net/index.html
Source0:        http://gts.sourceforge.net/tarballs/gts-snapshot-%{snapshot}.tar.gz
# Misc accumulated patches
Patch0:         0001-gts-snapshot-111025.patch
# Add manpage for gts2xyz (from debian)
Patch1:         0002-Add-gts2xyz-manpage.patch

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  netpbm-devel
BuildRequires:  make

%package devel
Summary:        Development files for gts
Requires:       pkgconfig
Requires:       glib2-devel
Requires:       %{name} = %{version}-%{release}

%description
GTS provides a set of useful functions to deal with 3D surfaces meshed
with interconnected triangles including collision detection,
multiresolution models, constrained Delaunay triangulations and robust
set operations (union, intersection, differences).

%description devel
This package contains the gts header files and libs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-snapshot-%{snapshot}
%patch -P0 -p1
%patch -P1 -p1

# Fix broken permissions
chmod +x test/*/*.sh

%build
%configure --disable-static --disable-dependency-tracking
%{make_build}

%install
%{make_install}
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# File names are too general, rename ...
mv -f $RPM_BUILD_ROOT%{_bindir}/delaunay $RPM_BUILD_ROOT%{_bindir}/gtsdelaunay 
mv -f $RPM_BUILD_ROOT%{_bindir}/happrox $RPM_BUILD_ROOT%{_bindir}/gtshapprox
mv -f $RPM_BUILD_ROOT%{_bindir}/transform $RPM_BUILD_ROOT%{_bindir}/gtstransform
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/delaunay.1 $RPM_BUILD_ROOT%{_mandir}/man1/gtsdelaunay.1 
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/happrox.1 $RPM_BUILD_ROOT%{_mandir}/man1/gtshapprox.1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/transform.1 $RPM_BUILD_ROOT%{_mandir}/man1/gtstransform.1

%check
# Urgh, something is very broken with gts rsp. its testsuite
make check ||:

%files
%license COPYING
%{_bindir}/gtsdelaunay
%{_bindir}/gts2dxf
%{_bindir}/gts2oogl
%{_bindir}/gts2stl
%{_bindir}/gtscheck
%{_bindir}/gtscompare
%{_bindir}/gtstemplate
%{_bindir}/gtshapprox
%{_bindir}/stl2gts
%{_bindir}/gtstransform
%{_bindir}/gts2xyz
%{_libdir}/*.so.*
%{_mandir}/man1/gtsdelaunay.1*
%{_mandir}/man1/gts2dxf.1*
%{_mandir}/man1/gts2oogl.1*
%{_mandir}/man1/gts2stl.1*
%{_mandir}/man1/gts2xyz.1*
%{_mandir}/man1/gtscheck.1*
%{_mandir}/man1/gtscompare.1*
%{_mandir}/man1/gtstemplate.1*
%{_mandir}/man1/gtshapprox.1*
%{_mandir}/man1/stl2gts.1*
%{_mandir}/man1/gtstransform.1*

%files devel
%{_bindir}/gts-config
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/aclocal/*
%{_mandir}/man1/gts-config.1*

%changelog
%autochangelog
