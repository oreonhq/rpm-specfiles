%global source0_hash 0d9ecb141de720e2fd4f7a275a4a83a961ffeb6717483d940021ffa1c46f665c
Name:           python-wsgiproxy2
Version:        0.5.1
Release:        1%{?dist}
Summary:        A WSGI Proxy with various http client backends
License:        MIT
URL:            https://github.com/gawel/WSGIProxy2/
Source0:        https://files.pythonhosted.org/packages/source/W/WSGIProxy2/WSGIProxy2-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wsgiproxy2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-wsgiproxy2
Summary:        A WSGI Proxy with various http client backends
%description -n python3-wsgiproxy2

%prep
%global oreon_srcdir WSGIProxy2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wsgiproxy2 usr/lib/python3*/site-packages/wsgiproxy2* usr/lib64/python3*/site-packages/wsgiproxy2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wsgiproxy2* usr/lib64/python3*/site-packages/wsgiproxy2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wsgiproxy2 -f %{oreon_filedir}/python3-wsgiproxy2.list

%changelog

%autochangelog
