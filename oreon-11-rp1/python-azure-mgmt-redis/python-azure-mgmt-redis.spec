%global source0_hash 5c3434c82492688e25b93aaf5113ecff0b92b7ad6da2a4fd4695530f82b152fa

# Upstream tests now require Docker + network access. 😢
%bcond_with    tests

%global         srcname         azure-mgmt-redis
%global         tarname         azure_mgmt_redis

Name:           python-%{srcname}
Version:        14.5.0
Release:        %autorelease
Summary:        Microsoft Azure Redis Cache Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarname} %{version}}

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
Microsoft Azure Redis Cache Management Client Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{tarname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

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

# LICENSE missing. Added PR to fix:
# https://github.com/Azure/azure-sdk-for-python/pull/20182
%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
