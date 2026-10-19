%global source0_hash bce09d52857857b22744f93241f16d5c62a1b118a7834e1c8afa14bebb964eee
Name:           python-djangoql
Version:        0.19.1
Release:        1%{?dist}
Summary:        DjangoQL: Advanced search language for Django
License:        MIT
URL:            https://github.com/ivelum/djangoql/
Source0:        https://files.pythonhosted.org/packages/source/d/djangoql/djangoql-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-djangoql = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-djangoql
Summary:        DjangoQL: Advanced search language for Django
%description -n python3-djangoql

%prep
%global oreon_srcdir djangoql-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-djangoql usr/lib/python3*/site-packages/djangoql* usr/lib64/python3*/site-packages/djangoql* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/djangoql* usr/lib64/python3*/site-packages/djangoql* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-djangoql -f %{oreon_filedir}/python3-djangoql.list

%changelog

%autochangelog
