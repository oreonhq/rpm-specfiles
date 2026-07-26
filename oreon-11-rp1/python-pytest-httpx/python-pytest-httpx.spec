%global source0_hash c0653073f7690ea1ab068cc5872655ff79634377441dce1f71ae7396721df915

%global pypi_name pytest-httpx

Name:           python-%{pypi_name}
Version:        0.35.0
Release:        %autorelease
Summary:        Send responses to httpx

License:        MIT
URL:            https://colin-b.github.io/pytest_httpx/
Source0:        https://github.com/Colin-b/pytest_httpx/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
httpx_mock pytest fixture will make sure every httpx request will be
replied to with user provided responses.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

%description -n python3-%{pypi_name}
httpx_mock pytest fixture will make sure every httpx request will be
replied to with user provided responses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pytest_httpx-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_httpx

%check
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
