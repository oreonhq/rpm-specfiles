%global source0_hash 242dcc6ce6b5b9bf621f5870c82a63997e8e82bc7c947f9ffe272b8f3dd5a780
Name:           python-respx
Version:        0.23.1
Release:        1%{?dist}
Summary:        A utility for mocking out the Python HTTPX and HTTP Core libraries.
License:        BSD-3-Clause
URL:            https://github.com/lundberg/respx
Source0:        https://files.pythonhosted.org/packages/source/r/respx/respx-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-respx = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-respx
Summary:        A utility for mocking out the Python HTTPX and HTTP Core libraries.
%description -n python3-respx

%prep
%global oreon_srcdir respx-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-respx usr/lib/python3*/site-packages/respx* usr/lib64/python3*/site-packages/respx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/respx* usr/lib64/python3*/site-packages/respx* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-respx -f %{oreon_filedir}/python3-respx.list

%changelog

%autochangelog
