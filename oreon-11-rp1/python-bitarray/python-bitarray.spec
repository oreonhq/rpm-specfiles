%global source0_hash bf19437ec00ec3d40aef82eaeedc14cf4000be9b635c4f5049796506e6630dd8
Name:           python-bitarray
Version:        3.11.0
Release:        1%{?dist}
Summary:        efficient arrays of booleans -- C extension
License:        PSF-2.0
URL:            https://github.com/ilanschnell/bitarray
Source0:        https://files.pythonhosted.org/packages/source/b/bitarray/bitarray-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42.0.0
Requires:       python3-bitarray = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-bitarray
Summary:        efficient arrays of booleans -- C extension
%description -n python3-bitarray

%prep
%global oreon_srcdir bitarray-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bitarray usr/lib/python3*/site-packages/bitarray* usr/lib64/python3*/site-packages/bitarray* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bitarray* usr/lib64/python3*/site-packages/bitarray* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bitarray -f %{oreon_filedir}/python3-bitarray.list

%changelog

%autochangelog
