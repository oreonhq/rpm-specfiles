%global source0_hash 58c1bdab4257d2551b9ef91cd48571f77b7c4d2bc45bf5e3c05ac97b3a4d7282

%global srcname xyzservices

Name:           python-%{srcname}
Version:        2024.6.0
Release:        %autorelease
Summary:        Source of XYZ tiles providers

License:        BSD-3-Clause
URL:            https://github.com/geopandas/xyzservices
Source0:        %pypi_source %{srcname}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
xyzservices is a lightweight library providing a repository of available XYZ
services offering raster basemap tiles. The repository is provided via Python
API and as a compressed JSON file. XYZ tiles can be used as background for your
maps to provide necessary spatial context.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3dist(mercantile)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)

%description -n python3-%{srcname}
xyzservices is a lightweight library providing a repository of available XYZ
services offering raster basemap tiles. The repository is provided via Python
API and as a compressed JSON file. XYZ tiles can be used as background for your
maps to provide necessary spatial context.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} -o 'markers=request'

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_datadir}/%{srcname}/

%changelog
%autochangelog
