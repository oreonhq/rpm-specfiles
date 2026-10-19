%global source0_hash adcc6a5cecdbd23ea25b095bd3ebb183c2c73fae03499c3d8e0ae932d73e8bb2
Name:           python-astdoc
Version:        1.3.2
Release:        1%{?dist}
Summary:        A lightweight Python library for parsing AST and extracting docstring information. Automatically generate documentation from Python source code by analyzing abstract syntax trees and docstrings.
License:        ...
URL:            https://github.com/daizutabi/astdoc
Source0:        https://files.pythonhosted.org/packages/source/a/astdoc/astdoc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-astdoc = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-astdoc
Summary:        A lightweight Python library for parsing AST and extracting docstring information. Automatically generate documentation from Python source code by analyzing abstract syntax trees and docstrings.
%description -n python3-astdoc

%prep
%global oreon_srcdir astdoc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-astdoc usr/lib/python3*/site-packages/astdoc* usr/lib64/python3*/site-packages/astdoc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/astdoc* usr/lib64/python3*/site-packages/astdoc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-astdoc -f %{oreon_filedir}/python3-astdoc.list

%changelog

%autochangelog
