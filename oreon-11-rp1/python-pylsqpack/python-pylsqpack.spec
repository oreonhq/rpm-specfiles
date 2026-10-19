%global source0_hash 8ec455f44614228f89e38d40c1b1e37895620e20ec6b21e3b562fa8b79a23890
Name:           python-pylsqpack
Version:        0.3.24
Release:        1%{?dist}
Summary:        Python wrapper for the ls-qpack QPACK library
License:        BSD-3-Clause
URL:            https://github.com/aiortc/pylsqpack
Source0:        https://files.pythonhosted.org/packages/source/p/pylsqpack/pylsqpack-%{version}.tar.gz
Patch0:         %{name}-unbundle_vendor_libs.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pylsqpack = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pylsqpack
Summary:        Python wrapper for the ls-qpack QPACK library
%description -n python3-pylsqpack

%prep
%global oreon_srcdir pylsqpack-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pylsqpack usr/lib/python3*/site-packages/pylsqpack* usr/lib64/python3*/site-packages/pylsqpack* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pylsqpack* usr/lib64/python3*/site-packages/pylsqpack* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pylsqpack -f %{oreon_filedir}/python3-pylsqpack.list

%changelog

%autochangelog
