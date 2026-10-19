%global source0_hash bea8294964266f6486f1ca514ccfcdbc54d4fe0d32882b38c1d4594df870be8b
Name:           python-mysqlclient
Version:        2.3.0
Release:        1%{?dist}
Summary:        Python interface to MySQL
License:        GPL-2.0-or-later
URL:            https://github.com/PyMySQL/mysqlclient
Source0:        https://files.pythonhosted.org/packages/source/m/mysqlclient/mysqlclient-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-mysqlclient = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mysqlclient
Summary:        Python interface to MySQL
%description -n python3-mysqlclient

%prep
%global oreon_srcdir mysqlclient-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mysqlclient usr/lib/python3*/site-packages/mysqlclient* usr/lib64/python3*/site-packages/mysqlclient* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mysqlclient* usr/lib64/python3*/site-packages/mysqlclient* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mysqlclient -f %{oreon_filedir}/python3-mysqlclient.list

%changelog

%autochangelog
