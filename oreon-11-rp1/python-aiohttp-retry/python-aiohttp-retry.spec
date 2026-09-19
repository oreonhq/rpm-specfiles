%global source0_hash 873fc4f7c5dde1206d7016d4d9889f0f6ea03bf5b6bafcb889bd407f0d97f84e

%global forgeurl https://github.com/inyutin/aiohttp_retry
Version:        2.9.1
%forgemeta

Name:           python-aiohttp-retry
Release:        %autorelease
Summary:        Simple retry client for aiohttp

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
# For testing:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(pytest-asyncio)

%global _description %{expand:
Simple retry client for aiohttp}

%description %_description

%package -n python3-aiohttp-retry
Summary:        %{summary}

%description -n python3-aiohttp-retry %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n aiohttp_retry-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aiohttp_retry

%check
%pytest --asyncio-mode=auto

%files -n python3-aiohttp-retry -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
