%global source0_hash 7ade9870ef1a96f392388fa397a34930860bb21fcf8a54ea090f0bdfb887ad21

Name:           quesoglc
Version:        0.7.2
Release:        44%{?dist}
Summary:        The OpenGL Character Renderer

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://quesoglc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-free.tar.bz2
Patch0:         quesoglc-0.7.2-drop-glewContext.patch
Patch1:         quesoglc-0.7.2-doxyfile.patch
Patch2:         fribidi.build.patch
Patch3:         quesoglc-0.7.2-wayland.patch
Patch4:         quesoglc-0.7.2-buildfix.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  fontconfig-devel
BuildRequires:  freeglut-devel
BuildRequires:  fribidi-devel
BuildRequires:  glew-devel
BuildRequires:  libSM-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXi-devel
BuildRequires:  libXi-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  doxygen
BuildRequires:  pkgconfig
BuildRequires:  texlive-epstopdf-bin
BuildRequires:  texlive-dvips-bin
BuildRequires:  ghostscript-core

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

%files
%doc AUTHORS ChangeLog README THANKS
%license COPYING
%{_libdir}/libGLC.so.*

%files devel
%doc docs/html
%{_includedir}/GL/glc.h
%{_libdir}/libGLC.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
