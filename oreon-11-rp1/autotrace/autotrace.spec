%global source0_hash 670d43797b37e067e0317e90e2c05eedeeb8ab630cf794c2abc1079a84120a68
Name:           autotrace
Version:        0.31.9
Release:        1%{?dist}
Summary:        Utility for converting bitmaps to vector graphics
License:        GPL-2.0-or-later and LGPL-2.1-or-later
URL:            http://autotrace.sourceforge.net/
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:	autotrace-0.31.9-pr105-ImageMagick7.patch
Patch1:	autotrace-0.31.9-expected-test-failure-no-imagemagick.patch
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libpng-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  procps-ng
BuildRequires:  pstoedit-devel
# /oreon:deps
%description
AutoTrace is a program for converting bitmaps to vector graphics.

Supported input formats include BMP, TGA, PNM, PPM, and any format
supported by ImageMagick, whereas output can be produced in
Postscript, SVG, xfig, SWF, and others.

%package devel
Summary:        Header files for autotrace
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       pstoedit-devel
%description devel
This package contains header files and development libraries for autotrace.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -ivf
%configure --without-magick --disable-static
%make_build
%install
%make_install
%find_lang %{name}
%oreon_autofiles autotrace-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n autotrace-devel -f %{oreon_filedir}/autotrace-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.31.9-1
- Prepare for Oreon 11 (RP1)
