%global source0_hash faa4d74d9354352f6db2c98c1dca2a7bbc2ea50e51fe5899c9b9b257b1eff2ee

%bcond tests 1

Name:           python-aiolimiter
Version:        1.2.1
Release:        %autorelease
Summary:        An efficient implementation of a rate limiter for asyncio

License:        MIT
URL:            https://github.com/mjpieters/aiolimiter
Source:         %{url}/archive/v%{version}/aiolimiter-%{version}.tar.gz

# https://github.com/mjpieters/aiolimiter/pull/312
Patch: 0001-tests-Prefer-tomllib-where-available.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-cov
%if 0%{?rhel} && 0%{?rhel} < 10
BuildRequires:  python3-toml
%endif
%endif

%global _description %{expand:
An efficient implementation of a rate limiter for asyncio.

This project implements the Leaky bucket algorithm, giving you precise
control over the rate a code section can be entered.}

%description %_description

%package -n python3-aiolimiter
Summary:        %{summary}

%description -n python3-aiolimiter %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n aiolimiter-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aiolimiter

%check
%pyproject_check_import

%if %{with tests}
%pytest tests
%endif

%files -n python3-aiolimiter -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md

%changelog
%autochangelog
