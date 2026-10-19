%global source0_hash none
Name:           scribus
Version:        1.6.5
Release:        1%{?dist}
Summary:        Desktop Publishing application written in Qt
License:        GPL-2.0-or-later AND OGL-UK-3.0 AND CC0-1.0 AND CC-BY-4.0 AND CC-BY-SA-4.0 AND LicenseRef-Fedora-Public-Domain AND Apache-2.0 AND LGPL-2.0-or-later
URL:            http://www.scribus.net/
Source0:        %{name}-%{version}-free.tar.xz
Patch:          scribus-1.6.5-poppler-26.01.0.patch
%filter_provides_in %{_libdir}/%{name}/plugins
%filter_setup
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  hyphen-devel
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libfreehand-0.1)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmspub-0.1)
BuildRequires:  pkgconfig(libpagemaker-0.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpodofo)
BuildRequires:  pkgconfig(libqxp-0.0)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzmf-0.0)
BuildRequires:  pkgconfig(openscenegraph)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(poppler-data)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-tkinter
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
Scribus is an desktop open source page layout program with
the aim of producing commercial grade output in PDF and
Postscript, primarily, though not exclusively for Linux.

While the goals of the program are for ease of use and simple easy to
understand tools, Scribus offers support for professional publishing
features, such as CMYK color, easy PDF creation, Encapsulated Postscript
import/export and creation of color separations.

%prep

%autosetup -p1

# fix permissions
chmod a-x scribus/pageitem_latexframe.h

# drop shebang lines from python scripts
%py3_shebang_fix %{name}/plugins/scriptplugin/{samples,scripts}/*.py

%build

%cmake  \
        -DWANT_CCACHE=YES \
        -DWANT_CPP17=ON \
        -DWANT_DISTROBUILD=YES \
        -DWANT_GRAPHICSMAGICK=1 \
        -DWANT_HUNSPELL=1 \
%if "%{_lib}" == "lib64"
        -DWANT_LIB64=YES \
%endif
        -DWANT_NORPATH=1 \
        -DWITH_BOOST=1 \
        -DWITH_PODOFO=1
%cmake_build
%install
%cmake_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
        %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
