%global source0_hash 00f16db782f4a13c78c5804aedc434e46794a77e89999a168f9401106270e50a
Name:           python-llvmlite
Version:        0.49.0
Release:        1%{?dist}
Summary:        lightweight wrapper around basic LLVM functionality
License:        BSD-2-Clause AND Apache-2.0 WITH LLVM-exception
URL:            https://github.com/numba/llvmlite
Source0:        https://files.pythonhosted.org/packages/source/l/llvmlite/llvmlite-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-llvmlite = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-llvmlite
Summary:        lightweight wrapper around basic LLVM functionality
%description -n python3-llvmlite

%prep
%global oreon_srcdir llvmlite-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-llvmlite usr/lib/python3*/site-packages/llvmlite* usr/lib64/python3*/site-packages/llvmlite* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/llvmlite* usr/lib64/python3*/site-packages/llvmlite* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-llvmlite -f %{oreon_filedir}/python3-llvmlite.list

%changelog

%autochangelog
