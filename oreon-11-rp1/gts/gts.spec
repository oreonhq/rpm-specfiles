%global source0_hash c23f72ab74bbf65599f8c0b599d6336fabe1ec2a09c19b70544eeefdc069b73b
%global snapshot 121130
Name:           gts
Version:        0.7.6
Release:        1%{?dist}
Summary:        GNU Triangulated Surface Library
License:        LGPL-2.0-or-later
URL:            http://gts.sourceforge.net/index.html
Source0:        http://%{name}.sourceforge.net/tarballs/%{name}-snapshot-%{snapshot}.tar.gz
Patch0:         0001-gts-snapshot-111025.patch
Patch1:         0002-Add-gts2xyz-manpage.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  netpbm-devel
# /oreon:deps
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
mv -f $RPM_BUILD_ROOT%{_bindir}/delaunay $RPM_BUILD_ROOT%{_bindir}/gtsdelaunay 
mv -f $RPM_BUILD_ROOT%{_bindir}/happrox $RPM_BUILD_ROOT%{_bindir}/gtshapprox
mv -f $RPM_BUILD_ROOT%{_bindir}/transform $RPM_BUILD_ROOT%{_bindir}/gtstransform
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/delaunay.1 $RPM_BUILD_ROOT%{_mandir}/man1/gtsdelaunay.1 
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/happrox.1 $RPM_BUILD_ROOT%{_mandir}/man1/gtshapprox.1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/transform.1 $RPM_BUILD_ROOT%{_mandir}/man1/gtstransform.1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check ||:
%files -f %{oreon_filedir}/main.list
%files -n gts-devel -f %{oreon_filedir}/gts-devel.list

%changelog

%autochangelog
