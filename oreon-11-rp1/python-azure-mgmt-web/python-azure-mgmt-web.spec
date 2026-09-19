%global source0_hash 4455ecd3b498577085c1904e6d17139254e358ba07fe6c4835a891bbaf7b06c2

# No tests provided. 😢
%bcond_with    tests

%global         srcname     azure-mgmt-web
%global         tarball_name     azure_mgmt_web

Name:           python-%{srcname}
Version:        9.0.0
Release:        %autorelease
Summary:        Microsoft Azure Web Apps Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{version}}

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
Microsoft Azure Web Apps Management Client Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{tarball_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure

%if %{with tests}
%check
%pyproject_check_import
%pytest --disable-warnings
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
