%global source0_hash 3caf9f5a4164611122d412bc11b2f9114fd29c85e1ba27bb38060d3c236bdc8d
Name:           python-aiohttp-socks
Version:        0.12.0
Release:        1%{?dist}
Summary:        Proxy connector for aiohttp
License:        Apache-2.0
URL:            https://github.com/romis2012/aiohttp-socks
Source0:        https://files.pythonhosted.org/packages/source/a/aiohttp_socks/aiohttp_socks-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-aiohttp-socks = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aiohttp-socks
Summary:        Proxy connector for aiohttp
# oreon:reqs
Requires:       python3dist(aiohttp) >= 3.10.0
Requires:       python3dist(python-socks[asyncio]) < 4.0.0
Requires:       python3dist(python-socks[asyncio]) >= 2.4.3
# /oreon:reqs
%description -n python3-aiohttp-socks

%prep
%global oreon_srcdir aiohttp_socks-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiohttp-socks usr/lib/python3*/site-packages/aiohttp_socks* usr/lib64/python3*/site-packages/aiohttp_socks* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiohttp_socks* usr/lib64/python3*/site-packages/aiohttp_socks* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aiohttp-socks -f %{oreon_filedir}/python3-aiohttp-socks.list

%changelog

%autochangelog
