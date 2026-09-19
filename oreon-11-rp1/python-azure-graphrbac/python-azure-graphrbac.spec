%global source0_hash d0bb62d8bf8e196b903f3971ba4afa448e4fe14e8394ebfcdd941d84d62ecafe

# Tests are missing VCR recordings. 📼
%bcond_with     tests

%global         srcname     azure-graphrbac

Name:           python-%{srcname}
Version:        0.60.0
Release:        %autorelease
Summary:        Microsoft Azure Graph RBAC Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

Epoch:          1

BuildArch:      noarch

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
Microsoft Azure Graph RBAC Client Library for Python}

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
%doc README.rst

%changelog
%autochangelog
