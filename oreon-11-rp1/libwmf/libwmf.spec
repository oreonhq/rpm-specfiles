%global source0_hash 18ba69febd2f515d98a2352de284a8051896062ac9728d2ead07bc39ea75a068

Summary: Windows MetaFile Library
Name: libwmf
Version: 0.2.13
Release: 9%{?dist}
#libwmf is under the LGPLv2+, however...
#1. The tarball contains an old version of the urw-fonts under GPL+.
#   Those fonts are not installed
#2. The header of the command-line wmf2plot utility places it under the GPLv2+.
#   wmf2plot is neither built or install
License: LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-1.0-or-later
Source:        https://github.com/caolanm/libwmf/archive/refs/tags/v0.2.13.tar.gz

URL: https://github.com/caolanm/libwmf

Patch0: 1f87c35bc2a36fdca760a4577761d30d9cc876e2.patch

Provides: bundled(gd) = 2.0.0

Requires: urw-fonts
Requires: %{name}-lite = %{version}-%{release}

# for file triggers
Requires: gdk-pixbuf2%{?_isa} >= 2.31.5-2.fc24

BuildRequires: freetype-devel, gdk-pixbuf2-devel, libtool, libxml2-devel, libpng-devel
BuildRequires: libjpeg-devel, libXt-devel, libX11-devel, dos2unix, libtool
BuildRequires: make

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
f=README ; iconv -f iso-8859-2 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f

%patch -P 0 -p1

%build
autoreconf -i -f -Ipatches
%configure --with-libxml2 --disable-static --disable-dependency-tracking --with-gsfontdir=/usr/share/fonts/urw-base35
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

rm -rf $RPM_BUILD_ROOT%{_includedir}/libwmf/gd
find doc -name "Makefile*" -exec rm {} \;

#we're carrying around duplicate fonts
rm -rf $RPM_BUILD_ROOT%{_datadir}/libwmf/fonts/*afm
rm -rf $RPM_BUILD_ROOT%{_datadir}/libwmf/fonts/*t1
sed -i $RPM_BUILD_ROOT%{_datadir}/libwmf/fonts/fontmap -e 's#libwmf/fonts#fonts/urw-base35#g'

%ldconfig_scriptlets
%ldconfig_scriptlets lite

%files
%{_libdir}/libwmf-0.2.so.7*
%{_libdir}/gdk-pixbuf-2.0/*/loaders/*.so
%{_bindir}/wmf2svg
%{_bindir}/wmf2gd
%{_bindir}/wmf2eps
%{_bindir}/wmf2fig
%{_bindir}/wmf2x
%{_bindir}/libwmf-fontmap
%{_datadir}/libwmf/

%files lite
%doc AUTHORS README
%license COPYING
%{_libdir}/libwmflite-0.2.so.7*

%files devel
%doc doc/*.html
%doc doc/*.png
%doc doc/*.gif
%doc doc/html
%doc doc/caolan
%{_libdir}/libwmf*.so
%{_libdir}/pkgconfig/libwmf.pc
%{_includedir}/libwmf/
%{_bindir}/libwmf-config


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.13-9
- Prepare for Oreon 11 (RP1)
