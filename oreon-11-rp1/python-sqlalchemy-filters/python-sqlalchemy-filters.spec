%global source0_hash fbbdd98c7dd1e122b4b8ec979514d39d5fc72d3835086f8c013705aa52b2e2a6

%global pypi_name sqlalchemy-filters

Name:           python-%{pypi_name}
Version:        0.12.0
Release:        23%{?dist}
Summary:        A library to filter SQLAlchemy queries

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/juliotrigo/sqlalchemy-filters
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Filter, sort and paginate SQLAlchemy query
objects. Ideal for exposing these actions over a REST API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(six) >= 1.10
Requires:       python3dist(sqlalchemy) >= 1.0.16
Requires:       python3dist(sqlalchemy) < 2
%description -n python3-%{pypi_name}
Filter, sort and paginate SQLAlchemy query
objects. Ideal for exposing these actions over a REST API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# Tests are not included in the tarball

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sqlalchemy_filters
%{python3_sitelib}/sqlalchemy_filters-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
