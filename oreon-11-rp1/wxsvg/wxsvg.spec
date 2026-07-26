%global source0_hash 5bf6ac6831b54bd19aef48cde8fa0572dbb63f30aee9d5323f6be6b3f326534b

Name:          wxsvg
Version:       1.5.25
Release:       7%{?dist}
Summary:       C++ library to create, manipulate and render SVG files
License:       LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:           https://sourceforge.net/projects/wxsvg
Source0:       https://downloads.sourceforge.net/wxsvg/wxsvg-%{version}.tar.bz2

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: expat-devel
BuildRequires: libexif-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: wxGTK-devel

%description
wxSVG is C++ library to create, manipulate and render Scalable Vector Graphics
(SVG) files with the wxWidgets toolkit.

%package devel
Summary: Development files for the wxSVG library
Group: Development/Libraries

%description devel
wxSVG is C++ library to create, manipulate and render Scalable Vector Graphics
(SVG) files with the wxWidgets toolkit.

This package provides the files required to develop programs that use wxsvg.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static

%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_bindir}/svgview
%{_libdir}/libwxsvg.so.3{,.*}

%files devel
%{_includedir}/wxSVG/
%{_includedir}/wxSVGXML/
%{_libdir}/libwxsvg.so
%{_libdir}/pkgconfig/libwxsvg.pc

%changelog
%autochangelog
