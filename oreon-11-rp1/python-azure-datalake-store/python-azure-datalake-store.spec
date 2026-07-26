%global source0_hash 5364d4445aab154a1c7cb10215629c3ce46ce5c7aaaf16071890c03fae53a035

# No tests are included with this version of azure-datalake-store.
%bcond_with     tests

%global         srcname     azure-datalake-store
%global         tarball_name    azure_datalake_store

Name:           python-%{srcname}
Version:        1.0.1
Release:        %autorelease
Summary:        Azure Data Lake Store Filesystem Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{version}}

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
Azure Data Lake Store Filesystem Client Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{tarball_name}-%{version}

# Fix incorrect line endings in the README.
sed -i 's/\r$//' README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure

# Remove the samples since many of them are empty or have wrong line endings.
rm -rf %{buildroot}%{python3_sitelib}/samples

%check
%pyproject_check_import -e 'samples*'

%if %{with tests}
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst HISTORY.rst

%changelog
%autochangelog
