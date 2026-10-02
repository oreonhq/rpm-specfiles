%global source0_hash 0943132b5db8de6b6a7f1d162682173e8763c7ed94e80fd39113292845f67762

%global qt_module qtimageformats

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

Summary: Qt6 - QtImageFormats component
Name:    qt6-%{qt_module}
Version: 6.12.0
Release: %autorelease

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

Patch0:  qtimageformats-fix-build.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: libtiff-devel
BuildRequires: jasper-devel
BuildRequires: pkgconfig(libmng)
BuildRequires: pkgconfig(libwebp)

# filter plugin provides
%global __provides_exclude_from ^%{_qt6_plugindir}/.*\\.so$

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
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1

rm -rv src/3rdparty


%build
%cmake_qt6 -DFEATURE_mng=ON

%cmake_build


%install
%cmake_install


%files
%license LICENSES/GPL*
%license LICENSES/LGPL*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_plugindir}/imageformats/libqmng.so
%{_qt6_plugindir}/imageformats/libqtga.so
%{_qt6_plugindir}/imageformats/libqtiff.so
%{_qt6_plugindir}/imageformats/libqwbmp.so
%{_qt6_plugindir}/imageformats/libqicns.so
%{_qt6_plugindir}/imageformats/libqjp2.so
%{_qt6_plugindir}/imageformats/libqwebp.so
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6Gui/*.cmake

%changelog
%autochangelog
