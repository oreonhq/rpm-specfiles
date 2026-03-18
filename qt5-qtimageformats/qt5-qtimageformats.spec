%global qt_module qtimageformats

Summary: Qt5 - QtImageFormats component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

## upstream patches
## repo: https://invent.kde.org/qt/qt/qtimageformats
## branch: kde/5.15
## git format-patch v5.15.18-lts-lgpl
Patch1: 0001-webp-support-sequential-input-device-if-full-file-is.patch
Patch2: 0002-Explicitly-include-QVarLengthArray-header.patch


BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

BuildRequires: libmng-devel
BuildRequires: libtiff-devel
BuildRequires: jasper-devel
BuildRequires: libwebp-devel >= 0.4.4

# prior -devel subpkg contained only runtime cmake bits
Obsoletes: qt5-qtimageformats-devel < 5.4.0
Provides:  qt5-qtimageformats-devel = %{version}-%{release}

# filter plugin provides
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$

%description
The core Qt Gui library by default supports reading and writing image
files of the most common file formats: PNG, JPEG, BMP, GIF and a few more,
ref. Reading and Writing Image Files. The Qt Image Formats add-on module
provides optional support for other image file formats, including:
MNG, TGA, TIFF, WBMP.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1

rm -rv src/3rdparty


%build
%{qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}


%files
%license LICENSE.GPL*
%license LICENSE.LGPL*
%{_qt5_plugindir}/imageformats/libqmng.so
%{_qt5_plugindir}/imageformats/libqtga.so
%{_qt5_plugindir}/imageformats/libqtiff.so
%{_qt5_plugindir}/imageformats/libqwbmp.so
%{_qt5_plugindir}/imageformats/libqicns.so
%{_qt5_plugindir}/imageformats/libqjp2.so
%{_qt5_plugindir}/imageformats/libqwebp.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_*Plugin.cmake


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Prepare for Oreon 11 (RP1)
