%global source0_hash 8867fa6966aeae3fe854697c9fb7d429666ae7ae8edda9b77c87c8e616ba6c65

%global srcname geodatasets

Name:           python-%{srcname}
Version:        2023.12.0
Release:        %autorelease
Summary:        Spatial data examples

License:        BSD-3-Clause
URL:            https://github.com/geopandas/geodatasets
Source0:        %pypi_source geodatasets

BuildArch:      noarch

BuildRequires:  python3-devel
# Test requirements
BuildRequires:  python3-geopandas
BuildRequires:  python3-pytest

%global _description %{expand:
Fetch links or download and cache spatial data example files.

The geodatasets contains an API on top of a JSON with metadata of externally
hosted datasets containing geospatial information useful for illustrative and
educational purposes.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%{pytest} -m 'not request'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
