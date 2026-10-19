%global source0_hash 54ce6e5f6e6ebf51ff54e2857257d0ff5a16b528de9f2796a01ca212b5086d77
Name:           python-colcon-powershell
Version:        0.5.0
Release:        1%{?dist}
Summary:        Extension for colcon to provide PowerShell scripts.
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-powershell/
Source0:        https://files.pythonhosted.org/packages/source/c/colcon_powershell/colcon_powershell-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-colcon-powershell = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-colcon-powershell
Summary:        Extension for colcon to provide PowerShell scripts.
%description -n python3-colcon-powershell

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir colcon_powershell-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-colcon-powershell usr/lib/python3*/site-packages/colcon_powershell* usr/lib64/python3*/site-packages/colcon_powershell* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/colcon_powershell* usr/lib64/python3*/site-packages/colcon_powershell* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-colcon-powershell -f %{oreon_filedir}/python3-colcon-powershell.list

%changelog

%autochangelog
