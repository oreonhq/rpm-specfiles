%global source0_hash 534e86667e318ac353d24d041229d3f821316e0f3b659f2fd050adfcd4f3472f
Name:           python-pylero
Version:        0.2.0
Release:        1%{?dist}
Summary:        Python SDK for Polarion
License:        MIT
URL:            https://github.com/RedHatQE/pylero
Source0:        https://files.pythonhosted.org/packages/source/p/pylero/pylero-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
Requires:       python3-pylero = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pylero
Summary:        Python SDK for Polarion
%description -n python3-pylero

%prep
%global oreon_srcdir pylero-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pylero usr/lib/python3*/site-packages/pylero* usr/lib64/python3*/site-packages/pylero* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pylero* usr/lib64/python3*/site-packages/pylero* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pylero -f %{oreon_filedir}/python3-pylero.list

%changelog

%autochangelog
