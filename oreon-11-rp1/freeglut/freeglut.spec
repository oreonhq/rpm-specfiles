%global source0_hash 674dcaff25010e09e450aec458b8870d9e98c46f99538db457ab659b321d9989
%global source1_hash 376b2f89680a9cdea0289de4e633e2287dcd80ba887a7b77ee7281934e5d2a38

%global __cmake_in_source_build 1
Summary:        A freely licensed alternative to the GLUT library
Name:           freeglut
Version:        3.8.0
Release:        2%{?dist}
URL:            http://freeglut.sourceforge.net
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# For the manpages
Source1:        https://downloads.sourceforge.net/openglut/openglut-0.6.3-doc.tar.gz
Patch0:         common.patch

License:        MIT

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig libGLU-devel libXext-devel
BuildRequires:  libXi-devel libICE-devel
BuildRequires: make
# The virtual Provides below is present so that this freeglut package is a
# drop in binary replacement for "glut" which will satisfy rpm dependancies
# properly.  The Obsoletes tag is required in order for any pre-existing
# "glut" package to be removed and replaced with freeglut when upgrading to
# freeglut.  Note: This package will NOT co-exist with the glut package.
Provides:       glut = 3.7
Obsoletes:      glut < 3.7

%description
freeglut is a completely open source alternative to the OpenGL Utility Toolkit
(GLUT) library with an OSI approved free software license. GLUT was originally
written by Mark Kilgard to support the sample programs in the second edition
OpenGL 'RedBook'. Since then, GLUT has been used in a wide variety of practical
applications because it is simple, universally available and highly portable.

freeglut allows the user to create and manage windows containing OpenGL
contexts on a wide range of platforms and also read the mouse, keyboard and
joystick functions.


%package devel
Summary:        Freeglut developmental libraries and header files
Requires:       %{name} = %{version}-%{release}
Requires:       libGL-devel libGLU-devel
Provides:       glut-devel = 3.7
Obsoletes:      glut-devel < 3.7

%description devel
Developmental libraries and header files required for developing or compiling
software which links to the freeglut library, which is an open source
alternative to the popular GLUT library, with an OSI approved free software
license.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -a 1
%patch -P 0 -p0

%build
%cmake -DFREEGLUT_BUILD_STATIC_LIBS=OFF -DCMAKE_POLICY_VERSION_MINIMUM=3.5 .
%cmake_build


%install
%cmake_install

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man3
install -p -m 644 doc/man/*.3 $RPM_BUILD_ROOT/%{_mandir}/man3


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS ChangeLog README.md
# don't include contents of doc/ directory as it is mostly obsolete
%{_libdir}/libglut.so.3*

%files devel
%doc doc/html/*.png doc/html/*.html
%{_includedir}/GL/*.h
%{_libdir}/libglut.so
%{_libdir}/pkgconfig/glut.pc
%{_mandir}/man3/*
%{_libdir}/cmake/FreeGLUT/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.8.0-2
- Prepare for Oreon 11 (RP1)
