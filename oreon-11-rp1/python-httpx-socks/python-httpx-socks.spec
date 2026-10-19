%global source0_hash 9114898471eb0b2c1f67749f1d2b1c9d35c9f6c450d2f5c338033fc2d0af2d20
Name:           python-httpx-socks
Version:        0.13.1
Release:        1%{?dist}
Summary:        Proxy _HTTP, SOCKS_ transports for httpx
License:        Apache-2.0
URL:            https://github.com/romis2012/httpx-socks
Source0:        https://files.pythonhosted.org/packages/source/h/httpx_socks/httpx_socks-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-httpx-socks = %{version}-%{release}
# /oreon:deps
%package -n       python3-httpx-socks+asyncio
Summary:        Metapackage for python3-httpx-socks asyncio extras
Requires:       python3-httpx-socks = %{version}-%{release}
Requires:       python3dist(async-timeout) >= 5.0.1
Provides:       python3dist(httpx-socks[asyncio]) = %{version}-%{release}

%description -n python3-httpx-socks+asyncio
Metapackage for python3-httpx-socks asyncio extras.

%package -n       python3-httpx-socks+trio
Summary:        Metapackage for python3-httpx-socks trio extras
Requires:       python3-httpx-socks = %{version}-%{release}
Requires:       python3dist(trio) >= 0.30.0
Provides:       python3dist(httpx-socks[trio]) = %{version}-%{release}

%description -n python3-httpx-socks+trio
Metapackage for python3-httpx-socks trio extras.

%package -n       python3-httpx-socks+anyio
Summary:        Metapackage for python3-httpx-socks anyio extras
Requires:       python3-httpx-socks = %{version}-%{release}
Requires:       python3dist(anyio) >= 4.12.1
Requires:       python3dist(anyio) < 5.0.0
Provides:       python3dist(httpx-socks[anyio]) = %{version}-%{release}

%description -n python3-httpx-socks+anyio
Metapackage for python3-httpx-socks anyio extras.

%description

%package -n     python3-httpx-socks
Summary:        Proxy _HTTP, SOCKS_ transports for httpx
# oreon:reqs
Requires:       python3dist(httpcore) < 2.0
Requires:       python3dist(httpcore) >= 1.0
Requires:       python3dist(httpx) < 0.29.0
Requires:       python3dist(httpx) >= 0.28.0
Requires:       python3dist(python-socks) < 4.0.0
Requires:       python3dist(python-socks) >= 2.4.3
Requires:       python3dist(sniffio) >= 1.1.0
# /oreon:reqs
%description -n python3-httpx-socks

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir httpx_socks-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-httpx-socks usr/lib/python3*/site-packages/httpx_socks* usr/lib64/python3*/site-packages/httpx_socks* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/httpx_socks* usr/lib64/python3*/site-packages/httpx_socks* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-httpx-socks -f %{oreon_filedir}/python3-httpx-socks.list

%changelog

%autochangelog
