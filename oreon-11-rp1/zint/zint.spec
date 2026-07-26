%global source0_hash bce37d9b86e6127cac63c8b6267ac421116d4ac086519d726eb724f5462d98c7

Name:      zint
Version:   2.15.0
Release:   3%{?dist}
Summary:   Barcode generator library
License:   BSD-3-Clause AND GPL-3.0-or-later
URL:       http://www.zint.org.uk
Source:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz

# create shared libQZint instead of static one
Patch0:    %{name}-shared.patch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qttools-static
BuildRequires: desktop-file-utils

%description
Zint is a C library for encoding data in several barcode variants. The
bundled command-line utility provides a simple interface to the library.
Features of the library:
- Over 50 symbologies including all ISO/IEC standards, like QR codes.
- Unicode translation for symbologies which support Latin-1 and 
  Kanji character sets.
- Full GS1 support including data verification and automated insertion of 
  FNC1 characters.
- Support for encoding binary data including NULL (ASCII 0) characters.
- Health Industry Barcode (HIBC) encoding capabilities.
- Output in PNG, EPS and SVG formats with user adjustable sizes and colors.
- Verification stage for SBN, ISBN and ISBN-13 data.

%package devel
Summary:       Library and header files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      cmake

%description devel 
C library and header files needed to develop applications that use 
the Zint library. The API documentation can be found on the project website:
http://www.zint.org.uk/zintSite/Manual.aspx

%package qt
Summary:       Zint Barcode Studio

%description qt
Zint Barcode Studio is a Qt-based GUI which allows desktop users to generate 
barcodes which can then be embedded in documents or HTML pages.

%package qt-devel
Summary:       Library and header files for %{name}-qt
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}

%description qt-devel 
C library and header files needed to develop applications that use libQZint.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}-src

# fix line endings
sed -i "s|\r||g" docs/manual.txt

# remove BSD-licensed file required for Windows only (just to ensure that this package is plain GPLv3+)
rm -f backend/ms_stdint.h

# remove bundled getopt sources (we use the corresponding Fedora package instead)
rm -f frontend/getopt*.*

find -type f -exec chmod 644 {} \;

%build
%cmake
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}/%{_datadir}/apps
install -D -p -m 644 docs/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -D -p -m 644 cmake/modules/FindZint.cmake %{buildroot}%{_datadir}/cmake/Modules/FindZint.cmake
install -D -p -m 644 %{name}-qt.png %{buildroot}/usr/share/pixmaps/%{name}-qt.png
install -D -p -m 644 %{name}-qt.desktop %{buildroot}%{_datadir}/applications/%{name}-qt.desktop
mv %{buildroot}%{_datadir}/%{name} %{buildroot}%{_datadir}/cmake/%{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-qt.desktop

%ldconfig_scriptlets
%ldconfig_scriptlets qt

%files
%doc docs/manual.txt README TODO
%license LICENSE frontend/COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_libdir}/libzint.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/libzint.so
%{_datadir}/cmake/%{name}/
%{_datadir}/cmake/Modules/*.cmake

%files qt
%{_bindir}/%{name}-qt
%{_libdir}/libQZint.so.*
%{_datadir}/applications/%{name}-qt.desktop
%{_datadir}/pixmaps/%{name}-qt.png

%files qt-devel
%{_includedir}/qzint.h
%{_libdir}/libQZint.so

%changelog
%autochangelog
