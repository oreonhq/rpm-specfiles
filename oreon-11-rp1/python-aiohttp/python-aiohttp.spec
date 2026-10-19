%global source0_hash 9491196535a88924a60afd5b5f434b5b203b6cc616250878dbdb223a8f7844bc
Name:           python-aiohttp
Version:        3.14.3
Release:        1%{?dist}
Summary:        Async http client/server framework _asyncio_
License:        Apache-2.0 AND MIT
URL:            https://github.com/aio-libs/aiohttp
Source0:        https://files.pythonhosted.org/packages/source/a/aiohttp/aiohttp-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 67.0
Requires:       python3-aiohttp = %{version}-%{release}
# /oreon:deps
%package -n       python3-aiohttp+speedups
Summary:        Metapackage for python3-aiohttp speedups extras
Requires:       python3-aiohttp = %{version}-%{release}
Requires:       python3dist(aiodns) >= 3.3.0
Requires:       python3dist(brotli) >= 1.2
Requires:       python3dist(brotlicffi) >= 1.2
Provides:       python3dist(aiohttp[speedups]) = %{version}-%{release}

%description -n python3-aiohttp+speedups
Metapackage for python3-aiohttp speedups extras.

%description

%package -n     python3-aiohttp
Summary:        Async http client/server framework _asyncio_
# oreon:reqs
Requires:       python3dist(aiohappyeyeballs) >= 2.5.0
Requires:       python3dist(aiosignal) >= 1.4.0
Requires:       python3dist(async-timeout) < 6.0
Requires:       python3dist(async-timeout) >= 4.0
Requires:       python3dist(attrs) >= 17.3.0
Requires:       python3dist(frozenlist) >= 1.1.1
Requires:       python3dist(multidict) < 7.0
Requires:       python3dist(multidict) >= 4.5
Requires:       python3dist(propcache) >= 0.2.0
Requires:       python3dist(typing-extensions) >= 4.4
Requires:       python3dist(yarl) < 2.0
Requires:       python3dist(yarl) >= 1.17.0
# /oreon:reqs
%description -n python3-aiohttp

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir aiohttp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiohttp usr/lib/python3*/site-packages/aiohttp* usr/lib64/python3*/site-packages/aiohttp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiohttp* usr/lib64/python3*/site-packages/aiohttp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aiohttp -f %{oreon_filedir}/python3-aiohttp.list

%changelog

%autochangelog
