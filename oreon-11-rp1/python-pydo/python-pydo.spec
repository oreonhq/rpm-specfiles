%global source0_hash 77c7e97b1b7fe3ef9aeed2198e5846e06502585ed1ac6f255ee1f215e5f5deda

%global srcname pydo

Name: python-%{srcname}
Summary: PyDo - DigitalOcean python library
Version: 0.24.0
Release: 3%{?dist}

License: ASL 2.0

Url: https://github.com/digitalocean/%{srcname}
Source:         %{url}/archive/v%{version}/pydo-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3dist(poetry-core)
# Test dependencies
BuildRequires:  python3dist(aioresponses)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(responses)

%global _description %{expand:
Official DigitalOcean Python Client based on the DO OpenAPIv3 specification.}
%description %_description

%package -n python3-pydo
Summary: %{summary}
%description -n python3-pydo %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import
%pytest -rA --tb=short tests/mocked/.

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
