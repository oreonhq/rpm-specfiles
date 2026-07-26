%global source0_hash 119e34758e8088cdbb43ed81b4a6eaea88c764b0b7da19001a5514b2545501ce

Name:           spatialite-tools
Version:        5.1.0a
Release:        6%{?dist}
Summary:        A set of useful CLI tools for SpatiaLite

License:        GPL-3.0-or-later
Source0:        https://www.gaia-gis.it/gaia-sins/spatialite-tools-sources/%{name}-%{version}.tar.gz
URL:            https://www.gaia-gis.it/fossil/spatialite-tools

BuildRequires: make
BuildRequires:  expat-devel
BuildRequires:  freexl-devel
BuildRequires:  gcc
BuildRequires:  geos-devel
BuildRequires:  libspatialite-devel
BuildRequires:  librttopo-devel
BuildRequires:  libxml2-devel
BuildRequires:  minizip-devel
BuildRequires:  proj-devel
BuildRequires:  readline-devel
BuildRequires:  readosm-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel

%description
Spatialite-Tools is a set of useful CLI tools for SpatiaLite.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove unused Makefiles
rm -f Makefile-static*

%build
export LDFLAGS="%{__global_ldflags} -lxml2 -lm"
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS
%{_bindir}/exif_loader
%{_bindir}/shp_doctor
%{_bindir}/shp_sanitize
%{_bindir}/spatialite
%{_bindir}/spatialite_convert
%{_bindir}/spatialite_dem
%{_bindir}/spatialite_dxf
%{_bindir}/spatialite_gml
%{_bindir}/spatialite_network
%{_bindir}/spatialite_osm*
%{_bindir}/spatialite_tool
%{_bindir}/spatialite_xml_*
%{_bindir}/spatialite_xml2utf8

%changelog
%autochangelog
