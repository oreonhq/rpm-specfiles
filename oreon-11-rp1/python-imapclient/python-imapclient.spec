%global source0_hash 9c46f431ceecde87ae1bbb8c287cbeb20bc70bcbee3d0c3bd0c01808d28630f4
Name:           python-imapclient
Version:        4.0.1
Release:        1%{?dist}
Summary:        Easy-to-use, Pythonic and complete IMAP client library
License:        ...
URL:            https://github.com/mjs/imapclient/
Source0:        https://files.pythonhosted.org/packages/source/i/imapclient/imapclient-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-imapclient = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-imapclient
Summary:        Easy-to-use, Pythonic and complete IMAP client library
%description -n python3-imapclient

%prep
%global oreon_srcdir imapclient-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-imapclient usr/lib/python3*/site-packages/imapclient* usr/lib64/python3*/site-packages/imapclient* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/imapclient* usr/lib64/python3*/site-packages/imapclient* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-imapclient -f %{oreon_filedir}/python3-imapclient.list

%changelog

%autochangelog
