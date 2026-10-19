%global source0_hash 8f4711a0ab11ee43fda567371ef6d9487afdbd4f156ca093e8fb306f4cc685ae
Name:           python-krb5
Version:        0.10.0
Release:        1%{?dist}
Summary:        Kerberos API bindings for Python
License:        MIT
URL:            https://github.com/jborean93/pykrb5
Source0:        https://files.pythonhosted.org/packages/source/k/krb5/krb5-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) == 3.3.0
BuildRequires:  python3dist(setuptools) >= 42.0.0
Requires:       python3-krb5 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-krb5
Summary:        Kerberos API bindings for Python
%description -n python3-krb5

%prep
%global oreon_srcdir krb5-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-krb5 usr/lib/python3*/site-packages/krb5* usr/lib64/python3*/site-packages/krb5* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/krb5* usr/lib64/python3*/site-packages/krb5* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-krb5 -f %{oreon_filedir}/python3-krb5.list

%changelog

%autochangelog
