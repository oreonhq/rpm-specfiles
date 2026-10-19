%global source0_hash 89f6f0706e53e2492c0baebb13961acfedb1fadadda1dbcb7159572d3037d307
Name:           python-pulsectl-asyncio
Version:        1.3.2
Release:        1%{?dist}
Summary:        Asyncio frontend for the pulsectl Python bindings of libpulse
License:        MIT
URL:            https://github.com/mhthies/pulsectl-asyncio
Source0:        https://files.pythonhosted.org/packages/source/p/pulsectl_asyncio/pulsectl_asyncio-%{version}.tar.gz
BuildArch:      noarch
Patch:          python-pulsectl-24.12.0.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-pulsectl-asyncio = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pulsectl-asyncio
Summary:        Asyncio frontend for the pulsectl Python bindings of libpulse
# oreon:reqs
Requires:       python3dist(pulsectl) <= 24.12.0
Requires:       python3dist(pulsectl) >= 23.5.0
# /oreon:reqs
%description -n python3-pulsectl-asyncio

%prep
%global oreon_srcdir pulsectl_asyncio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pulsectl-asyncio usr/lib/python3*/site-packages/pulsectl_asyncio* usr/lib64/python3*/site-packages/pulsectl_asyncio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pulsectl_asyncio* usr/lib64/python3*/site-packages/pulsectl_asyncio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pulsectl-asyncio -f %{oreon_filedir}/python3-pulsectl-asyncio.list

%changelog

%autochangelog
