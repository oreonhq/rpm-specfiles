%global source0_hash 015db92a07b4b4c751fb9bf3fc4f82be7fa5b07f10e3f1d8e5d5f1fc00c968bd

%global pypi_name flask-talisman

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        17%{?dist}
Summary:        HTTP security headers for Flask

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/wntrblm/flask-talisman
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.9

%description
Talisman is a small Flask extension that handles setting HTTP headers
that can help protect against a few common web application security issues.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Talisman is a small Flask extension that handles setting HTTP headers
that can help protect against a few common web application security issues.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/flask_talisman
%{python3_sitelib}/flask_talisman-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
