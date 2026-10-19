%global source0_hash 05a56527484f7f4e8c856419ea379b8dc359c36801c4992fdb330f294c690356
Name:           python-pytest-httpx
Version:        0.36.2
Release:        1%{?dist}
Summary:        Send responses to httpx.
License:        MIT
URL:            https://github.com/Colin-b/pytest_httpx
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_httpx/pytest_httpx-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-httpx = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-httpx+testing
Summary:        Metapackage for python3-pytest-httpx testing extras
Requires:       python3-pytest-httpx = %{version}-%{release}
Requires:       python3dist(pytest-cov) == 7.*
Requires:       python3dist(pytest-asyncio) == 1.*
Provides:       python3dist(pytest-httpx[testing]) = %{version}-%{release}

%description -n python3-pytest-httpx+testing
Metapackage for python3-pytest-httpx testing extras.

%description

%package -n     python3-pytest-httpx
Summary:        Send responses to httpx.
# oreon:reqs
Requires:       python3dist(httpx) == 0.28.*
Requires:       python3dist(pytest) == 9.*
# /oreon:reqs
%description -n python3-pytest-httpx

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_httpx-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-httpx usr/lib/python3*/site-packages/pytest_httpx* usr/lib64/python3*/site-packages/pytest_httpx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_httpx* usr/lib64/python3*/site-packages/pytest_httpx* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-httpx -f %{oreon_filedir}/python3-pytest-httpx.list

%changelog

%autochangelog
