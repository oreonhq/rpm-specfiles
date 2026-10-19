%global source0_hash 556124ef52464f90a30d39ecf6c1acf375fdbafdd680e1d609f5b929bfc111e7
Name:           ogr2osm
Version:        1.2.1
Release:        1%{?dist}
Summary:        Convert ogr-readable files like shapefiles into .pbf or .osm data
License:        MIT
URL:            https://github.com/roelderickx/ogr2osm
Source0:        https://github.com/roelderickx/ogr2osm/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-protobuf
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ogr2osm = %{version}-%{release}
# /oreon:deps
%description
ogr2osm will read any data source that ogr can read and handle reprojection
for you. It takes a python file to translate external data source tags into
OSM tags, allowing you to use complicated logic. If no translation is
specified it will use an identity translation, carrying all tags from the
source to the .pbf or .osm output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pyproject_check_import -t
%files

%changelog

%autochangelog
