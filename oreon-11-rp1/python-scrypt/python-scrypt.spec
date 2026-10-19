%global source0_hash 0d212010ba8c2e55475ba6258f30cee4da0432017514d8f6e855b7f1f8c55c77
Name:           python-scrypt
Version:        0.9.4
Release:        1%{?dist}
Summary:        Bindings for the scrypt key derivation function library
License:        ...
URL:            https://github.com/holgern/py-scrypt
Source0:        https://files.pythonhosted.org/packages/source/s/scrypt/scrypt-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-scrypt = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-scrypt
Summary:        Bindings for the scrypt key derivation function library
%description -n python3-scrypt

%prep
%global oreon_srcdir scrypt-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-scrypt usr/lib/python3*/site-packages/scrypt* usr/lib64/python3*/site-packages/scrypt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/scrypt* usr/lib64/python3*/site-packages/scrypt* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-scrypt -f %{oreon_filedir}/python3-scrypt.list

%changelog

%autochangelog
