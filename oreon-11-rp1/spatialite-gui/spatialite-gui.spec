%global source0_hash ba48d96df18cebc3ff23f69797207ae1582cce62f4596b69bae300ca3c23db33

%global pre beta1

Name:           spatialite-gui
Version:        2.1.0
Release:        0.23%{?pre:.%pre}%{?dist}
Summary:        GUI to manage Spatialite databases

License:        GPL-3.0-or-later
URL:            https://www.gaia-gis.it/fossil/spatialite_gui
Source0:        http://www.gaia-gis.it/gaia-sins/spatialite-gui-sources/spatialite_gui-%{version}%{?pre:-%pre}.tar.gz
# Link agains wx aui
#Patch1:         %{name}-1.7.0-aui_linking.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  CharLS-devel
BuildRequires:  freexl-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpq-devel
BuildRequires:  libspatialite-devel
BuildRequires:  librasterlite2-devel
BuildRequires:  libxlsxwriter-devel
BuildRequires:  libwebp-devel
BuildRequires:  libxml2-devel
BuildRequires:  lz4-devel
BuildRequires:  libzstd-devel
BuildRequires:  minizip-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  wxGTK-devel
BuildRequires:  sqlite-devel
BuildRequires:  geos-devel
BuildRequires:  proj-devel
BuildRequires:  virtualpg-devel

%description
GUI to manage Spatialite databases.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n spatialite_gui-%{version}%{?pre:-%pre}

%build
%configure
%make_build

%install
%make_install

#desktop-file-install \
#    --dir=%{buildroot}%{_datadir}/applications \
#    gnome_resource/%{name}.desktop

%files
%doc AUTHORS
%license COPYING
%{_bindir}/spatialite_gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
