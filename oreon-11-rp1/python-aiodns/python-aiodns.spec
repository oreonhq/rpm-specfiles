%global source0_hash cb10e0c0d2591636716ad2fe402e977c16d71bdaf76bb8cb49e8a6633596f736
Name:           python-aiodns
Version:        4.0.4
Release:        1%{?dist}
Summary:        Simple DNS resolver for asyncio
License:        MIT
URL:            https://github.com/aio-libs/aiodns.git
Source0:        https://files.pythonhosted.org/packages/source/a/aiodns/aiodns-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aiodns = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aiodns
Summary:        Simple DNS resolver for asyncio
# oreon:reqs
Requires:       python3dist(pycares) < 6
Requires:       python3dist(pycares) >= 5.0.0
# /oreon:reqs
%description -n python3-aiodns

%prep
%global oreon_srcdir aiodns-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiodns usr/lib/python3*/site-packages/aiodns* usr/lib64/python3*/site-packages/aiodns* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiodns* usr/lib64/python3*/site-packages/aiodns* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aiodns -f %{oreon_filedir}/python3-aiodns.list

%changelog

%autochangelog
