%global source0_hash 2d5c1ed0f9fa60f200ba821ac5731fbc26ce7d2e0d023a3392b74c3590eafae5
Name:           python-managesieve
Version:        0.8.1
Release:        1%{?dist}
Summary:        RFC-5804 Manage Sieve client library for remotely managing Sieve scripts
License:        PSF-2.0 AND GPL-3.0-only
URL:            https://gitlab.com/htgoebel/managesieve/
Source0:        https://files.pythonhosted.org/packages/source/m/managesieve/managesieve-%{version}.tar.gz
BuildArch:      noarch
Patch:          fix_ssl_wrap_socket_error.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 39.2.0
Requires:       python3-managesieve = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-managesieve
Summary:        RFC-5804 Manage Sieve client library for remotely managing Sieve scripts
%description -n python3-managesieve

%prep
%global oreon_srcdir managesieve-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-managesieve usr/lib/python3*/site-packages/managesieve* usr/lib64/python3*/site-packages/managesieve* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/managesieve* usr/lib64/python3*/site-packages/managesieve* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-managesieve -f %{oreon_filedir}/python3-managesieve.list

%changelog

%autochangelog
