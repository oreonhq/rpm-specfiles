%global source0_hash da179160121f5b38be061dbff29cd2b60d5d029b2207102454d77a7114e64f97

# No tests from upstream yet.
%bcond_with     tests

%global         srcname     vsts

Name:           python-%{srcname}
Version:        0.1.25
Release:        %autorelease
Summary:        Azure DevOps Python API
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
This repository contains Python APIs for interacting with and managing Azure
DevOps. These APIs power the Azure DevOps Extension for Azure CLI.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

sed -i 's/,<0.7.0//' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import -e 'vsts.customer_intelligence.*'

%if %{with tests}
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
# No README included in pypi package. 😢

%changelog
%autochangelog
