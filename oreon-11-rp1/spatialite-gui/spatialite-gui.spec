%global source0_hash ba48d96df18cebc3ff23f69797207ae1582cce62f4596b69bae300ca3c23db33
%global pre beta1
Name:           spatialite-gui
Version:        2.1.0
Release:        1%{?dist}
Summary:        GUI to manage Spatialite databases
License:        GPL-3.0-or-later
URL:            https://www.gaia-gis.it/fossil/spatialite_gui
Source0:        http://www.gaia-gis.it/gaia-sins/%{name}-sources/spatialite_gui-%{version}-%{pre}.tar.gz
# oreon:deps
BuildRequires:  CharLS-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freexl-devel
BuildRequires:  gcc-c++
BuildRequires:  geos-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpq-devel
BuildRequires:  librasterlite2-devel
BuildRequires:  libspatialite-devel
BuildRequires:  libwebp-devel
BuildRequires:  libxlsxwriter-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  minizip-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  proj-devel
BuildRequires:  sqlite-devel
BuildRequires:  virtualpg-devel
BuildRequires:  wxGTK-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
