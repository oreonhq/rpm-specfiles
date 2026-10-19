%global source0_hash ec862c06b3138f669f89c00338dd99da64f41cec4111c644681f6b496523f1f1
Name:           python-molmass
Version:        2026.8.15
Release:        1%{?dist}
Summary:        Molecular mass calculations
License:        BSD-3-Clause
URL:            https://github.com/cgohlke/molmass
Source0:        https://files.pythonhosted.org/packages/source/m/molmass/molmass-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-molmass = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-molmass
Summary:        Molecular mass calculations
%description -n python3-molmass

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir molmass-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-molmass usr/lib/python3*/site-packages/molmass* usr/lib64/python3*/site-packages/molmass* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/molmass* usr/lib64/python3*/site-packages/molmass* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-molmass -f %{oreon_filedir}/python3-molmass.list

%changelog

%autochangelog
