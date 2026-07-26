%global source0_hash 3c2f64f754187c19e0a1a029b148b74cf58dd12ec27b4e19c0e5d6e22b5a9a86

%global pypi_name sentinels

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        2%{?dist}
Summary:        Various objects to denote special meanings in Python

License:        BSD-3-Clause
URL:            https://github.com/vmalloc/sentinels
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The sentinels module is a small utility providing the Sentinel class, along
with useful instances.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name}
The sentinels module is a small utility providing the Sentinel class, along
with useful instances.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sentinels

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
