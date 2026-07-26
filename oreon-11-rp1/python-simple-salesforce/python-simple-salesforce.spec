%global source0_hash c3dd30f1f36384ba3b030f16af5ba83690553c278442812e3a7b839e672c91a8

%global pypi_name simple-salesforce
%global pypi_version 1.12.5

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        12%{?dist}
Summary:        Simple Salesforce is a basic Salesforce.com REST API client built for Python
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/%{pypi_name}/%{pypi_name}
Source0:        %{url}/archive/v%{pypi_version}/%{pypi_name}-v%{pypi_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Tests requirements:
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(responses)

%global _description %{expand:
Simple Salesforce is a basic Salesforce.com REST API client built for Python.
The goal is to provide a very low-level interface to the REST Resource and APEX
API, returning a dictionary of the API JSON response. }

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{pypi_version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check
# Set timezone to prevent Pendulum error: `RuntimeError: Unable to find any timezone configuration`
export TZ=UTC
%pytest

%install
%pyproject_install
%pyproject_save_files simple_salesforce

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst docs/user_guide docs/changes.rst docs/conf.py
%license LICENSE.txt

%changelog
%autochangelog
