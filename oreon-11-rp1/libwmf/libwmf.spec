%global source0_hash 50f36f939b751274b5f0abef9fb38c23c101ebf8bba0934cfbf5444ec37011f0
Summary:        Windows MetaFile Library
Name: libwmf
Version: 0.2.16
Release:        1%{?dist}
License: LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-1.0-or-later
Source0:        https://github.com/caolanm/libwmf/archive/refs/tags/v%{version}.tar.gz#/libwmf-%{version}.tar.gz
URL: https://github.com/caolanm/libwmf
Provides: bundled(gd) = 2.0.0
Requires: urw-fonts
Requires: %{name}-lite = %{version}-%{release}
Requires: gdk-pixbuf2%{?_isa} >= 2.31.5-2.fc24
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  freetype-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%description
A library for reading and converting Windows MetaFile vector graphics (WMF).

%package lite
Summary: Windows Metafile parser library
%description lite
A library for parsing Windows MetaFile vector graphics (WMF).

%package devel
Summary: Support files necessary to compile applications with libwmf
Requires: libwmf = %{version}-%{release}
Requires: freetype-devel, libX11-devel, libxml2-devel, libjpeg-devel, libpng-devel
%description devel
Libraries, headers, and support files necessary to compile applications 
using libwmf.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
f=README ; iconv -f iso-8859-2 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f

%build

autoreconf -i -f -Ipatches
%configure --with-libxml2 --disable-static --disable-dependency-tracking --with-gsfontdir=/usr/share/fonts/urw-base35
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_includedir}/libwmf/gd
find doc -name "Makefile*" -exec rm {} \;
rm -rf $RPM_BUILD_ROOT%{_datadir}/libwmf/fonts/*afm
rm -rf $RPM_BUILD_ROOT%{_datadir}/libwmf/fonts/*t1
sed -i $RPM_BUILD_ROOT%{_datadir}/libwmf/fonts/fontmap -e 's#libwmf/fonts#fonts/urw-base35#g'
%ldconfig_scriptlets
%ldconfig_scriptlets lite
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libwmf-lite -f %{oreon_filedir}/libwmf-lite.list
%files -n libwmf-devel -f %{oreon_filedir}/libwmf-devel.list

%changelog

%autochangelog
