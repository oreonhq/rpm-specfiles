# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 674dcaff25010e09e450aec458b8870d9e98c46f99538db457ab659b321d9989
%global source1_hash 376b2f89680a9cdea0289de4e633e2287dcd80ba887a7b77ee7281934e5d2a38
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global __cmake_in_source_build 1
Summary:        A freely licensed alternative to the GLUT library
Name:           freeglut
Version:        3.8.0
Release:        %{autorelease}
URL:            http://freeglut.sourceforge.net
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/openglut/openglut-0.6.3-doc.tar.gz
Patch0:         common.patch

License:        MIT

BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  libGLU-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libICE-devel
BuildRequires: make
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
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
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
%{_libdir}/libglut.so.3*

%files devel
%doc doc/html/*.png doc/html/*.html
%{_includedir}/GL/*.h
%{_libdir}/libglut.so
%{_libdir}/pkgconfig/glut.pc
%{_mandir}/man3/*
%{_libdir}/cmake/FreeGLUT/*

%changelog
%autochangelog
