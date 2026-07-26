%global source0_hash 4437c29cf8ecf96f68e2dfa9e0abe1a125bd9d772d9ee7413d48cbf6092d9e01

%global srcname mercantile

Name:           python-%{srcname}
Version:        1.2.1
Release:        21%{?dist}
Summary:        Web Mercator XYZ tile utilities

License:        BSD-3-Clause
URL:            https://github.com/mapbox/mercantile
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(numpydoc)

%global _description %{expand:\
Mercantile is a module of utilities for working with XYZ style Spherical
Mercator tiles (as in Google Maps, OSM, Mapbox, etc.) and includes a set of
command line programs built on these utilities.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# remove the sphinx-build leftovers
rm -rf html/.{buildinfo,doctrees}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest}

%files -n python3-%{srcname}  -f %{pyproject_files}
%doc README.rst html
%license LICENSE.txt
%{_bindir}/mercantile

%changelog
%autochangelog
