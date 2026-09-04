%global source0_hash 94bc100c32862e09817f019fc9c44ded625fe52a5f338b3168117fcf84c178a7

Name:           python-async-lru
Version:        2.1.0
Release:        %autorelease
Summary:        Simple lru_cache for asyncio
# SPDX
License:        MIT
URL:            https://github.com/aio-libs/async_lru
Source:         https://github.com/aio-libs/async-lru/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-timeout

%global _description %{expand:
This package is 100% port of Python built-in
function functools.lru_cache for asyncio.}

%description %_description

%package -n     python3-async-lru
Summary:        %{summary}

%description -n python3-async-lru %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n async-lru-%{version}
# Removing pytest CLI options. Most of them are related to coverage.
sed -i "/addopts/d" setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files async_lru

%check
# Ignore DeprecationWarning untill
# https://github.com/aio-libs/async-lru/issues/635
# is resolved.
%pytest -W ignore::DeprecationWarning

%files -n python3-async-lru -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
