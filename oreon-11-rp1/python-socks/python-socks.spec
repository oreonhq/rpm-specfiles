%global source0_hash 6d97a84f30db3d6827479d6df5f2ddefeab242c59c5c8d61d4cf1aa761a10b3f
%global undername python_socks
Name:           python-socks
Version:        2.7.2
Release:        1%{?dist}
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python
License:        Apache-2.0
URL:            https://github.com/romis2012/%{name}
Source0:        https://github.com/romis2012/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-socks = %{version}-%{release}
# /oreon:deps
%package -n       python3-socks+asyncio
Summary:        Metapackage for python3-socks asyncio extras
Requires:       python3-socks = %{version}-%{release}
Requires:       python3dist(async-timeout) >= 4.0
Provides:       python3dist(socks[asyncio]) = %{version}-%{release}

%description -n python3-socks+asyncio
Metapackage for python3-socks asyncio extras.

%package -n       python3-socks+trio
Summary:        Metapackage for python3-socks trio extras
Requires:       python3-socks = %{version}-%{release}
Requires:       python3dist(trio) >= 0.24
Provides:       python3dist(socks[trio]) = %{version}-%{release}

%description -n python3-socks+trio
Metapackage for python3-socks trio extras.

%package -n       python3-socks+curio
Summary:        Metapackage for python3-socks curio extras
Requires:       python3-socks = %{version}-%{release}
Requires:       python3dist(curio) >= 1.4
Provides:       python3dist(socks[curio]) = %{version}-%{release}

%description -n python3-socks+curio
Metapackage for python3-socks curio extras.

%package -n       python3-socks+anyio
Summary:        Metapackage for python3-socks anyio extras
Requires:       python3-socks = %{version}-%{release}
Requires:       python3dist(anyio) >= 3.3.4
Requires:       python3dist(anyio) < 5.0.0
Provides:       python3dist(socks[anyio]) = %{version}-%{release}

%description -n python3-socks+anyio
Metapackage for python3-socks anyio extras.

%description

%package -n python3-socks
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Obsoletes:      python3-socks+curio < 2.0.3-7
%description -n python3-socks

# extras: asyncio, trio

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

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-socks usr/lib/python3*/site-packages/socks* usr/lib64/python3*/site-packages/socks* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/socks* usr/lib64/python3*/site-packages/socks* usr/bin/*

%check

%pytest tests/
%files
%files -n python3-socks -f %{oreon_filedir}/python3-socks.list

%changelog

%autochangelog
