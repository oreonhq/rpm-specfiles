%global source0_hash 08b5e25de58f21ce71dc7db3b3b8106c1fa776f3024c54e45b45b374e89234c9
Name:           python-xlrd
Version:        2.0.2
Release:        1%{?dist}
Summary:        Library for developers to extract data from Microsoft Excel _tm_ .xls spreadsheet files
License:        ...
URL:            http://www.python-excel.org/
Source0:        https://files.pythonhosted.org/packages/source/x/xlrd/xlrd-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xlrd = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xlrd
Summary:        Library for developers to extract data from Microsoft Excel _tm_ .xls spreadsheet files
%description -n python3-xlrd

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir xlrd-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xlrd usr/lib/python3*/site-packages/xlrd* usr/lib64/python3*/site-packages/xlrd* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xlrd* usr/lib64/python3*/site-packages/xlrd* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xlrd -f %{oreon_filedir}/python3-xlrd.list

%changelog

%autochangelog
