%global source0_hash 0629ef7738773582739647201f2ed6fdcb95dbd81643c0f070a0a189b4ed2f46

%bcond tests %{undefined rhel}

Name:           python-respx
Version:        0.23.1
Release:        %autorelease
Summary:        Utility for mocking out the HTTPX and HTTP Core libraries

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://lundberg.github.io/respx/
Source0:        https://github.com/lundberg/respx/archive/%{version}/respx-%{version}.tar.gz
BuildArch:      noarch

%description
An utility for mocking out the Python HTTPX and HTTP Core libraries.

%package -n     python3-respx
Summary:        %{summary}

BuildRequires:  python3-devel
%if %{with tests}
# Test requirements
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(trio)
%endif

%description -n python3-respx
An utility for mocking out the Python HTTPX and HTTP Core libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n respx-%{version} -p1
# We don't care about coverage in downstream builds,
# and running it is against the Python Packaging Guidelines.
sed -i -e '/--cov/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files respx

%check
%if %{with tests}
%pytest -v tests -k "not test_pass_through" --asyncio-mode=auto
%endif

%files -n python3-respx -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
