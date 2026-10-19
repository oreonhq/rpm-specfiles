%global source0_hash dc8a74b5632b2c3fc84d33c2bf6ee43210b71b8ddf0a3166a25aeb46620bfa27
Summary:        A Tubing and Extrusion Library for OpenGL
Name: libgle
Version: 3.1.0
Release:        1%{?dist}
License: GPL-2.0-only OR (ClArtistic AND LicenseRef-Callaway-MIT)
URL: http://www.linas.org/gle/
Source0:        http://www.linas.org/gle/pub/gle-%{version}.tar.gz
Patch0: libgle-examples-makefile.patch
Patch1: libgle-configure-c99.patch
Patch2: libgle-pr13-function-type-cast.patch
# oreon:deps
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
# /oreon:deps
%description
The GLE Tubing and Extrusion Library consists of a number of "C"
language subroutines for drawing tubing and extrusions. It is a very
fast implementation of these shapes, outperforming all other
implementations, most by orders of magnitude. It uses the
OpenGL programming API to perform the actual drawing of the tubing
and extrusions.

%package devel
Requires: glut-devel
Requires: libGL-devel
Requires: libGLU-devel
Requires: libX11-devel
Requires: libXext-devel
Requires: libXi-devel
Requires: libXmu-devel
Requires: libXmu-devel
Requires: libXt-devel
Summary: GLE includes and development libraries
%description devel
Includes, man pages, and development libraries for the GLE Tubing and
Extrusion Library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gle-%{version}
%patch -P0 -p5
%patch -P1 -p1
%patch -P2 -p1
# Prevent re-running autotools.
touch -r Makefile.am aclocal.m4 configure*

%build

%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mv $RPM_BUILD_ROOT%{_docdir}/gle docs
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgle-devel -f %{oreon_filedir}/libgle-devel.list

%changelog

%autochangelog
