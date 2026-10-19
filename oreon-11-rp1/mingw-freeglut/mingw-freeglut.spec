%global source0_hash 9c3d4d6516fbfa0280edc93c77698fb7303e443c1aaaf37d269e3288a6c3ea52
%{?mingw_package_header}
Name:           mingw-freeglut
Version:        3.6.0
Release:        1%{?dist}
Summary:        Fedora MinGW alternative to the OpenGL Utility Toolkit (GLUT)
License:        MIT
URL:            https://freeglut.sourceforge.net/
Source0:        https://downloads.sourceforge.net/freeglut/freeglut-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library with an OSI approved free software
license. GLUT was originally written by Mark Kilgard to support the
sample programs in the second edition OpenGL 'RedBook'. Since then,
GLUT has been used in a wide variety of practical applications because
it is simple, universally available and highly portable.

freeglut allows the user to create and manage windows containing
OpenGL contexts on a wide range of platforms and also read the mouse,
keyboard and joystick functions.

# Win32
%package -n mingw32-freeglut
Summary:        Fedora MinGW alternative to the OpenGL Utility Toolkit (GLUT)
%description -n mingw32-freeglut
freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library with an OSI approved free software
license. GLUT was originally written by Mark Kilgard to support the
sample programs in the second edition OpenGL 'RedBook'. Since then,
GLUT has been used in a wide variety of practical applications because
it is simple, universally available and highly portable.

freeglut allows the user to create and manage windows containing
OpenGL contexts on a wide range of platforms and also read the mouse,
keyboard and joystick functions.

# Win64
%package -n mingw64-freeglut
Summary:        Fedora MinGW alternative to the OpenGL Utility Toolkit (GLUT)
%description -n mingw64-freeglut
freeglut is a completely open source alternative to the OpenGL Utility
Toolkit (GLUT) library with an OSI approved free software
license. GLUT was originally written by Mark Kilgard to support the
sample programs in the second edition OpenGL 'RedBook'. Since then,
GLUT has been used in a wide variety of practical applications because
it is simple, universally available and highly portable.

freeglut allows the user to create and manage windows containing
OpenGL contexts on a wide range of platforms and also read the mouse,
keyboard and joystick functions.

%package -n mingw64-freeglut-static
Summary:        Static version of the MinGW freeglut library
Requires:       mingw64-freeglut = %{version}-%{release}
%description -n mingw64-freeglut-static
Static version of the Fedora MinGW alternative to the OpenGL Utility
Toolkit (GLUT).

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n freeglut-%{version}

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%mingw_cmake -DFREEGLUT_REPLACE_GLUT:BOOL=ON
%mingw_make %{?_smp_mflags}
%install
%mingw_make_install
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libglut.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libglut.la
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libglut.a
%oreon_autofiles mingw32-freeglut usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-freeglut usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-freeglut-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-freeglut -f %{oreon_filedir}/mingw32-freeglut.list
%files -n mingw64-freeglut -f %{oreon_filedir}/mingw64-freeglut.list
%files -n mingw64-freeglut-static -f %{oreon_filedir}/mingw64-freeglut-static.list

%changelog

%autochangelog
