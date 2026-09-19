%global source0_hash 9b1ed0127459a66014aec3c56bebd93da3c1bc8bb6618c8082039a44889a755d

Name:           python-httpx-sse
Version:        0.4.3
Release:        %autorelease
Summary:        Consume Server-Sent Event (SSE) messages with HTTPX.
License:        MIT
URL:            https://github.com/florimondmanca/httpx-sse
Source:         %{pypi_source httpx_sse}

# Patch setup.cfg to remove --cov options from the pytest cli args.
Patch:          remove-coverage-options-from-pytest.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-httpx
BuildRequires:  python3-sse-starlette
# Dependencies for testing
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

%global _description %{expand:
Consume Server-Sent Event (SSE) messages with HTTPX.}

%description %_description

%package -n     python3-httpx-sse
Summary:        %{summary}

%description -n python3-httpx-sse %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n httpx_sse-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l httpx_sse

%check
%pyproject_check_import
%pytest

%files -n python3-httpx-sse -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
