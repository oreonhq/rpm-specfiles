%global source0_hash bf86000a21a1280f7a8aaf12dd9a10e59e778169653b53c86ad8f346fb39c066
%global qt_module qtimageformats
Summary:        Qt5 - QtImageFormats component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Patch1: 0001-webp-support-sequential-input-device-if-full-file-is.patch
Patch2: 0002-Explicitly-include-QVarLengthArray-header.patch
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Obsoletes: qt5-qtimageformats-devel < 5.4.0
Provides:  qt5-qtimageformats-devel = %{version}-%{release}
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$
# oreon:deps
BuildRequires:  jasper-devel
BuildRequires:  libmng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1

rm -rv src/3rdparty

%build

%{qmake_qt5}
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtimageformats-examples -f %{oreon_filedir}/qt5-qtimageformats-examples.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
