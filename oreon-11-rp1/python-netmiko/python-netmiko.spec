%global source0_hash 94cf7bfe5daed1d058444ce1637e10177df22f903683a53d1fbee47553488c65
Name:           python-netmiko
Version:        4.7.0
Release:        1%{?dist}
Summary:        Multi-vendor library to simplify legacy CLI connections to network devices
License:        MIT
URL:            https://github.com/ktbyers/netmiko
Source0:        https://files.pythonhosted.org/packages/source/n/netmiko/netmiko-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-netmiko = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-netmiko
Summary:        Multi-vendor library to simplify legacy CLI connections to network devices
%description -n python3-netmiko

%prep
%global oreon_srcdir netmiko-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-netmiko usr/lib/python3*/site-packages/netmiko* usr/lib64/python3*/site-packages/netmiko* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/netmiko* usr/lib64/python3*/site-packages/netmiko* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-netmiko -f %{oreon_filedir}/python3-netmiko.list

%changelog

%autochangelog
