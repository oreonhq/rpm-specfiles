%global source0_hash be54b7f3fa167bb83e4fcd936b887b708f4e57fe75911c02aebf53efaf8d938e
Name:           python-multipart
Version:        0.0.32
Release:        1%{?dist}
Summary:        A streaming multipart parser for Python
License:        Apache-2.0
URL:            https://github.com/Kludex/python-multipart
Source0:        https://files.pythonhosted.org/packages/source/p/python_multipart/python_multipart-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-multipart = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-python-multipart
Summary:        A streaming multipart parser for Python
%description -n python3-python-multipart

%prep
%global oreon_srcdir python_multipart-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-python-multipart usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-python-multipart -f %{oreon_filedir}/python3-python-multipart.list

%changelog

%autochangelog
