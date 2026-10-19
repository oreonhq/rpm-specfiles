%global source0_hash 039af6d18f2683184e85a28ca5de4c24de6e6f33db9287403b44ebd113754910
Name:           python-u-boot-pylib
Version:        0.0.7
Release:        1%{?dist}
Summary:        U-Boot python library
License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org
Source0:        https://files.pythonhosted.org/packages/source/u/u_boot_pylib/u_boot_pylib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-u-boot-pylib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-u-boot-pylib
Summary:        U-Boot python library
%description -n python3-u-boot-pylib

%prep
%global oreon_srcdir u_boot_pylib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-u-boot-pylib usr/lib/python3*/site-packages/u_boot_pylib* usr/lib64/python3*/site-packages/u_boot_pylib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/u_boot_pylib* usr/lib64/python3*/site-packages/u_boot_pylib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-u-boot-pylib -f %{oreon_filedir}/python3-u-boot-pylib.list

%changelog

%autochangelog
