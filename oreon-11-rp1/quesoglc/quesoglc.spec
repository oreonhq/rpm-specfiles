%global source0_hash 7ade9870ef1a96f392388fa397a34930860bb21fcf8a54ea090f0bdfb887ad21
Name:           quesoglc
Version:        0.7.2
Release:        1%{?dist}
Summary:        The OpenGL Character Renderer
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://quesoglc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-free.tar.bz2
Patch0:         quesoglc-0.7.2-drop-glewContext.patch
Patch1:         quesoglc-0.7.2-doxyfile.patch
Patch2:         fribidi.build.patch
Patch3:         quesoglc-0.7.2-wayland.patch
Patch4:         quesoglc-0.7.2-buildfix.patch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  freeglut-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-core
BuildRequires:  glew-devel
BuildRequires:  libSM-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pkgconfig
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-epstopdf-bin
# /oreon:deps
%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libGL-devel
Requires:       pkgconfig
%description
The OpenGL Character Renderer (GLC) is a state machine that provides OpenGL
programs with character rendering services via an application programming
interface (API).

%description devel
This package provides the libraries, include files, and other resources needed
for developing GLC applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -f include/GL/{glxew,wglew,glew}.h
rm -f src/glew.c
ln -s %{_includedir}/GL/{glxew,wglew,glew}.h include/GL/
rm -rf src/fribidi/

%build

%configure --disable-static 
%make_build
cd docs
doxygen
cd ../
%install
%make_install
rm %{buildroot}%{_libdir}/libGLC.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n quesoglc-devel -f %{oreon_filedir}/quesoglc-devel.list

%changelog

%autochangelog
