%global source0_hash 59549c4c4068f26466b1097b574a8e5099fb2cd6c8be0a00395b06d3b29e278d

# EPEL9 does not have python-aiohttp packaged yet.
%if 0%{?fedora}
%bcond_without  tests
%else
%bcond_with     tests
%endif

%global         srcname     azure-mgmt-devtestlabs

Name:           python-%{srcname}
Version:        4.0.0
Release:        %autorelease
Summary:        Microsoft Azure DevTestLabs Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure DevTestLabs Management Client Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure

%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst HISTORY.rst

%changelog
%autochangelog
