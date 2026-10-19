%global source0_hash e8a5aa092dab2e1cbb9b94392036827b808dc37eb6cf1b1ab33c81957b3f5fe2
Name:           python-tftpy
Version:        0.8.7
Release:        1%{?dist}
Summary:        A TFTP protocol library for Python
License:        MIT
URL:            https://github.com/msoulier/tftpy
Source0:        https://files.pythonhosted.org/packages/source/t/tftpy/tftpy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-tftpy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tftpy
Summary:        A TFTP protocol library for Python
%description -n python3-tftpy

%prep
%global oreon_srcdir tftpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tftpy usr/lib/python3*/site-packages/tftpy* usr/lib64/python3*/site-packages/tftpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tftpy* usr/lib64/python3*/site-packages/tftpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tftpy -f %{oreon_filedir}/python3-tftpy.list

%changelog

%autochangelog
