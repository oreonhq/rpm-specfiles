%global source0_hash 0d6736a08c0b1e10e6197224ef512951514204706514244bd01aea49fd1442b3

%global srcname mapclassify

Name:           python-%{srcname}
Version:        2.10.0
Release:        %autorelease
Summary:        Classification Schemes for Choropleth Maps

License:        BSD-3-Clause
URL:            https://github.com/pysal/mapclassify
Source:         %pypi_source %{srcname}
# Test example datasets.
Source1:        https://geodacenter.github.io/data-and-lab/data/south.zip
# Don't use the network.
Patch:          0001-Use-system-copy-of-Natural-Earth-data.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli

# Tests
BuildRequires:  natural-earth-map-data-110m
BuildRequires:  python3dist(pytest-mpl)

%description
mapclassify is an open-source python library for Choropleth map classification.
It is part of PySAL the Python Spatial Analysis Library.

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
mapclassify is an open-source python library for Choropleth map classification.
It is part of PySAL the Python Spatial Analysis Library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem project.optional-dependencies.tests \
    'pytest-cov\b.*'

mkdir -p pysal_data/pysal
unzip %SOURCE1 -d pysal_data/pysal/South

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
export XDG_DATA_HOME=$PWD/pysal_data
%{pytest} --mpl

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
