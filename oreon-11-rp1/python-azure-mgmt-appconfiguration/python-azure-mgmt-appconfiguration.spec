%global source0_hash f8f0f81b790d1ed77bbc052ecdcf7b13091fad88b10c1f3f471000dbd9c20977

# Upstream hasn't packaged tests.
%bcond_with    tests

%global         srcname      azure-mgmt-appconfiguration
%global         tarball_name azure_mgmt_appconfiguration

Name:           python-%{srcname}
Version:        5.0.0
Release:        %autorelease
Summary:        Microsoft Azure App Configuration Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{version}}

BuildArch:      noarch

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
Microsoft Azure App Configuration Management Client Library for Python}

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{tarball_name}-%{version}

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
%doc README.md CHANGELOG.md

%changelog
%autochangelog
