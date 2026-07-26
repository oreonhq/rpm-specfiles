%global source0_hash ee1daf461e4942e9e6629cc74e60c03dd545fa28a71a0f4181fc5d50355cbb93

%global project_name QtPBFImagePlugin

%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$

Name:           qt5-qtpbfimageformat
Version:        3.1
Release:        6%{?dist}
Summary:        Qt image plugin for displaying Mapbox vector tiles

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/tumic0/QtPBFImagePlugin/

Source0:        https://github.com/tumic0/%{project_name}/archive/%{version}/%{project_name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  protobuf-lite-devel

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

%files
%license LICENSE
%doc README.md
%{_qt5_plugindir}/imageformats/libpbf.so

%changelog
%autochangelog
