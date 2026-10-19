%global source0_hash 9be861636b52cf978ac009261f133990d332ab4b82331fa6f3fb25e69bd375a3
Name:           sage
Version:        0.2.0
Release:        1%{?dist}
Summary:        OpenGL extensions library using SDL
License:        LGPL-2.0-or-later
URL:            http://worldforge.org/dev/eng/libraries/sage
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.gz
Patch0:         sage-0.1.2-noopt.patch
Patch1: sage-configure-c99.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Sage is an OpenGL extensions library using SDL. It aims to simplify the use of
checking for and loading OpenGL extensions in an application.

%package devel
Summary:        Development files for sage
Requires: pkgconfig %{name} = %{version}-%{release}
%description devel
Libraries and header files for developing applications that use sage.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
touch -r configure.ac configure.ac.stamp
%patch -P0 -p0
%patch -P1 -p1
touch -r configure.ac.stamp configure.ac
rm -f sage/glxext_sage.h
rm -f sage/wglext_sage.h

%build

%configure --disable-static
%make_build
%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{name}.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n sage-devel -f %{oreon_filedir}/sage-devel.list

%changelog

%autochangelog
