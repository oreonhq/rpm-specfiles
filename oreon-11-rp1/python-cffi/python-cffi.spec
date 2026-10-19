%global source0_hash dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be
Name:           python-cffi
Version:        2.1.1
Release:        1%{?dist}
Summary:        Foreign Function Interface for Python calling C code.
License:        MIT-0
URL:            https://github.com/python-cffi/cffi
Source0:        https://files.pythonhosted.org/packages/source/c/cffi/cffi-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-cffi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cffi
Summary:        Foreign Function Interface for Python calling C code.
%description -n python3-cffi

%prep
%global oreon_srcdir cffi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cffi usr/lib/python3*/site-packages/cffi* usr/lib64/python3*/site-packages/cffi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cffi* usr/lib64/python3*/site-packages/cffi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cffi -f %{oreon_filedir}/python3-cffi.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-1
- Prepare for Oreon 11 (RP1)
