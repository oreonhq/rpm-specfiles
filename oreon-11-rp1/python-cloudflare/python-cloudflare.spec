%global source0_hash 0ca2fb6017e8077bd798211d2505aa2cad186a2dac14a20aae57b8ffe43fb38b
Name:           python-cloudflare
Version:        5.7.0
Release:        1%{?dist}
Summary:        The official Python library for the cloudflare API
License:        Apache-2.0
URL:            https://github.com/cloudflare/cloudflare-python
Source0:        https://files.pythonhosted.org/packages/source/c/cloudflare/cloudflare-%{version}.tar.gz
BuildArch:      noarch
Patch0:         remove-jsonlines.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) == 1.26.3
Requires:       python3-cloudflare = %{version}-%{release}
# /oreon:deps
%package -n       python3-cloudflare+aiohttp
Summary:        Metapackage for python3-cloudflare aiohttp extras
Requires:       python3-cloudflare = %{version}-%{release}
Requires:       python3dist(httpx-aiohttp) >= 0.1.9
Provides:       python3dist(cloudflare[aiohttp]) = %{version}-%{release}

%description -n python3-cloudflare+aiohttp
Metapackage for python3-cloudflare aiohttp extras.

%description

%package -n     python3-cloudflare
Summary:        The official Python library for the cloudflare API
# oreon:reqs
Requires:       python3dist(anyio) < 5
Requires:       python3dist(anyio) >= 3.5.0
Requires:       python3dist(distro) < 2
Requires:       python3dist(distro) >= 1.7.0
Requires:       python3dist(httpx) < 1
Requires:       python3dist(httpx) >= 0.23.0
Requires:       python3dist(pydantic) < 3
Requires:       python3dist(pydantic) >= 1.9.0
Requires:       python3dist(typing-extensions) < 5
Requires:       python3dist(typing-extensions) >= 4.14
# /oreon:reqs
%description -n python3-cloudflare

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cloudflare-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cloudflare usr/lib/python3*/site-packages/cloudflare* usr/lib64/python3*/site-packages/cloudflare* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cloudflare* usr/lib64/python3*/site-packages/cloudflare* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cloudflare -f %{oreon_filedir}/python3-cloudflare.list

%changelog

%autochangelog
