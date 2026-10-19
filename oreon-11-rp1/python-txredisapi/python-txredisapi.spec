%global source0_hash 98e2440ff2e297c9048c5f9d516e7b1302d447cd9cd4568c986c35a8523de3c7
Name:           python-txredisapi
Version:        1.4.12
Release:        1%{?dist}
Summary:        non-blocking redis client for python
License:        ...
URL:            http://github.com/IlyaSkriblovsky/txredisapi
Source0:        https://files.pythonhosted.org/packages/source/t/txredisapi/txredisapi-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-txredisapi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-txredisapi
Summary:        non-blocking redis client for python
%description -n python3-txredisapi

%prep
%global oreon_srcdir txredisapi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-txredisapi usr/lib/python3*/site-packages/txredisapi* usr/lib64/python3*/site-packages/txredisapi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/txredisapi* usr/lib64/python3*/site-packages/txredisapi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-txredisapi -f %{oreon_filedir}/python3-txredisapi.list

%changelog

%autochangelog
