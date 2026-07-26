%global source0_hash 9c3d4d6516fbfa0280edc93c77698fb7303e443c1aaaf37d269e3288a6c3ea52

%{?mingw_package_header}

Name:           mingw-freeglut
Version:        3.6.0
Release:        6%{?dist}
Summary:        Fedora MinGW alternative to the OpenGL Utility Toolkit (GLUT)

License:        MIT

URL:            https://freeglut.sourceforge.net/
Source0:        https://downloads.sourceforge.net/freeglut/freeglut-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

BuildRequires:  make
BuildRequires:  cmake

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
# TODO: Please submit an issue to upstream (rhbz#2380897)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%mingw_cmake -DFREEGLUT_REPLACE_GLUT:BOOL=ON
%mingw_make %{?_smp_mflags}

%install
%mingw_make_install

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libglut.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libglut.la

# No mingw32-freeglut-static as libglut.a is already part of mingw32-crt
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libglut.a

%files -n mingw32-freeglut
%license COPYING
%doc AUTHORS ChangeLog README.md
%{mingw32_bindir}/libglut.dll
%{mingw32_libdir}/libglut.dll.a
%dir %{mingw32_includedir}/GL/
%{mingw32_includedir}/GL/freeglut.h
%{mingw32_includedir}/GL/freeglut_ext.h
%{mingw32_includedir}/GL/freeglut_std.h
%{mingw32_includedir}/GL/freeglut_ucall.h
%{mingw32_includedir}/GL/glut.h
%dir %{mingw32_libdir}/cmake/FreeGLUT/
%{mingw32_libdir}/cmake/FreeGLUT/FreeGLUT*.cmake
%{mingw32_libdir}/pkgconfig/glut.pc

%files -n mingw64-freeglut
%license COPYING
%doc AUTHORS ChangeLog README.md
%{mingw64_bindir}/libglut.dll
%{mingw64_libdir}/libglut.dll.a
%dir %{mingw64_includedir}/GL/
%{mingw64_includedir}/GL/freeglut.h
%{mingw64_includedir}/GL/freeglut_ext.h
%{mingw64_includedir}/GL/freeglut_std.h
%{mingw64_includedir}/GL/freeglut_ucall.h
%{mingw64_includedir}/GL/glut.h
%dir %{mingw64_libdir}/cmake/FreeGLUT/
%{mingw64_libdir}/cmake/FreeGLUT/FreeGLUT*.cmake
%{mingw64_libdir}/pkgconfig/glut.pc

%files -n mingw64-freeglut-static
%{mingw64_libdir}/libglut.a

%changelog
%autochangelog
