%global source0_hash aa5cb816553bb6647b63eec5e7528aa9a1d17ce1d5a43f4cb58cc13f56d33a1b

%global pypi_name pyopnsense
%global pkg_name opnsense

Name:           python-%{pkg_name}
Version:        0.3.0
Release:        22%{?dist}
Summary:        Python API client for OPNsense

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/mtreinish/pyopnsense
Source0:        %{pypi_source}
# Maintainers, please upstream
Patch0:         python-opnsense-rm-python-mock-usage.diff

BuildArch:      noarch

%description
A Python API client for the OPNsense API. This module provides a Python
interface for interacting with the OPNsense API.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(stestr)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
A Python API client for the OPNsense API. This module provides a Python
interface for interacting with the OPNsense API.

%package -n python-%{pkg_name}-doc
Summary:        pyopnsense documentation

BuildRequires:  python3dist(sphinx)
%description -n python-%{pkg_name}-doc
Documentation for pyopnsense.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 doc/source html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest -v pyopnsense/tests

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pkg_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
