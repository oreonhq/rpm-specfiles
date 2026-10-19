%global source0_hash 92805abc84505e3e7e27aec775ab0754ecb4182fe2d8ff2a9d568ccdcb2811ac
%global _cmake_generator "Unix Makefiles"
%global srcname fltk
Name:		    fltk1.3
Version:	    1.3.11
Release:        1%{?dist}
Summary:        C++ user interface toolkit
License:	    LGPL-2.0-or-later WITH FLTK-exception
URL:            http://www.fltk.org/
Source0:        https://github.com/%{srcname}/%{srcname}/releases/download/release-%{version}/%{srcname}-%{version}-source.tar.gz
Source1:        fltk-config.sh
Patch0:         fltk-cmake.patch
Patch1:         fltk-1.3.4-fltk_config.patch
Patch2:         mingw-fltk-cmake.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  texlive-latex
# /oreon:deps
%description
\

%package devel
Summary:        Development files for %{name}
Conflicts:      fltk-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(gl) pkgconfig(glu)
Requires:       pkgconfig(ice) pkgconfig(sm)
Requires:       pkgconfig(xft) pkgconfig(xt) pkgconfig(x11)
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libpng)
Requires:       pkgconfig(zlib)
%description devel
%{summary}.

%package static
Summary:        Static libraries for %{name}
Conflicts:      fltk-static
Requires:       %{name}-devel = %{version}-%{release}
%description static
%{summary}.

%package fluid
Summary:        Fast Light User Interface Designer for FLTK 1.3
Conflicts:      fltk-fluid
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel
%description fluid
%{summary}, an interactive GUI designer for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%conf
%cmake -DFLTK_CONFIG_PATH:PATH=%{_libdir}/cmake/fltk \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DOPTION_BUILD_HTML_DOCUMENTATION:BOOL=ON \
       -DOPTION_BUILD_PDF_DOCUMENTATION:BOOL=OFF \
       -DOPTION_BUILD_SHARED_LIBS:BOOL=ON

%build

%cmake_build
%cmake_build --target docs
%install
%cmake_install
mv src/xutf8/COPYING ./COPYING.xutf8
%ifarch x86_64 %{ix86}
%global arch %(uname -m 2>/dev/null || echo undefined)
mv $RPM_BUILD_ROOT%{_bindir}/fltk-config \
   $RPM_BUILD_ROOT%{_bindir}/fltk-config-%{arch}
install -p -m755 -D %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/fltk-config
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n fltk1.3-devel -f %{oreon_filedir}/fltk1.3-devel.list
%files -n fltk1.3-static -f %{oreon_filedir}/fltk1.3-static.list
%files -n fltk1.3-fluid -f %{oreon_filedir}/fltk1.3-fluid.list

%changelog

%autochangelog
