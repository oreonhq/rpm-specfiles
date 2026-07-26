%global source0_hash 6d97a84f30db3d6827479d6df5f2ddefeab242c59c5c8d61d4cf1aa761a10b3f

%global undername python_socks

%global _description %{expand:
The python-socks package provides a core proxy client functionality for Python.
Supports SOCKS4(a), SOCKS5, HTTP (tunneling) proxy and provides sync and async
(asyncio, trio) APIs. It is used internally by aiohttp-socks and
httpx-socks packages.
}

Name:           python-socks
Version:        2.7.2
Release:        %autorelease
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python

License:        Apache-2.0
URL:            https://github.com/romis2012/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-socks
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# curio is discontinued upstream and not ready for Python 3.12
Obsoletes:      python3-socks+curio < 2.0.3-7

%description -n python3-socks %_description

# extras: asyncio, trio
%pyproject_extras_subpkg -n python3-socks asyncio trio anyio

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# Also, remove curio, and all exact and upper bounds on test dep. versions.
sed -r \
    -e 's/^(pytest-cov|coveralls|flake8)\b/# &/' \
    -e 's/^(curio)\b/# &/' \
    -e 's/(==|,<).*//' \
    requirements-dev.txt |
  tee requirements-dev-filtered.txt

%generate_buildrequires
%pyproject_buildrequires -x asyncio,trio,anyio requirements-dev-filtered.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{undername}

%check
# https://github.com/romis2012/python-socks/blob/master/.travis.yml
%pytest tests/

%files -n python3-socks -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
