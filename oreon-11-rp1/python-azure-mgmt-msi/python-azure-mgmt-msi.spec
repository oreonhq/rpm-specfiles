%global source0_hash 1a01a089f1f66cb0d4b2886603d5ba415f360eff0be6f685737ecdd59c78225b

# No tests included yet.
%bcond_with     tests

%global         srcname     azure-mgmt-msi

Name:           python-%{srcname}
Version:        7.1.0
Release:        %autorelease
Summary:        Microsoft Azure MSI Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source azure_mgmt_msi %{version}}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure MSI Management Client Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_mgmt_msi-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif

%install
%pyproject_install
%pyproject_save_files -l azure

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
