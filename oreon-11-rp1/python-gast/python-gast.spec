%global source0_hash 0bb14cd1b806722e91ddbab6fb86bba148c22b40e7ff11e248974e04c8adfdae
Name:           python-gast
Version:        0.7.0
Release:        1%{?dist}
Summary:        Python AST that abstracts the underlying Python version
License:        ...
URL:            https://github.com/serge-sans-paille/gast/
Source0:        https://files.pythonhosted.org/packages/source/g/gast/gast-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gast = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-gast
Summary:        Python AST that abstracts the underlying Python version
%description -n python3-gast

%prep
%global oreon_srcdir gast-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gast usr/lib/python3*/site-packages/gast* usr/lib64/python3*/site-packages/gast* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gast* usr/lib64/python3*/site-packages/gast* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gast -f %{oreon_filedir}/python3-gast.list

%changelog

%autochangelog
