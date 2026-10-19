%global source0_hash 319c9460ddc4bb412842e793c789f9dd5ee718c6d5a069d9ef2d36c19e4cfd8a
%global project_name QtPBFImagePlugin
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$
Name:           qt5-qtpbfimageformat
Version:        5.2
Release:        1%{?dist}
Summary:        Qt image plugin for displaying Mapbox vector tiles
License:        GPL-3.0-only
URL:            https://github.com/tumic0/QtPBFImagePlugin/
Source0:        https://github.com/tumic0/%{project_name}/archive/%{version}/%{project_name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  protobuf-lite-devel
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
QtPBFImagePlugin is a Qt image plugin that enables applications capable
of displaying raster MBTiles maps or raster XYZ online maps to also display
PBF(MVT) vector tiles without (almost, see usage) any application modifications.

Standard Mapbox GL Styles are used for styling the maps. Most relevant style
features used by Maputnik are supported. The style is loaded from the
$AppDataLocation/style/style.json file on plugin load. If the style uses
a sprite, the sprite JSON file must be named sprite.json and the sprite image
sprite.png and both files must be placed in the same directory as the style
itself. A default fallback style (OSM-Liberty) for OpenMapTiles is part
of the plugin.

"Plain" PBF files as well as gzip compressed files (as used in MBTiles)
are supported by the plugin.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{project_name}-%{version}

%build

%{qmake_qt5} pbfplugin.pro
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
