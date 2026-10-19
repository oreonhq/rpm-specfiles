%global source0_hash 6f36ce644881db5cd8940bee9b7cb3f3f6b7b327ba8a67d83d3e2caa0538bf9d
Name:           python-dicttoxml
Version:        1.7.16
Release:        1%{?dist}
Summary:        Converts a Python dictionary or other native data type into a valid XML string.
License:        ...
URL:            https://github.com/quandyfactory/dicttoxml
Source0:        https://files.pythonhosted.org/packages/source/d/dicttoxml/dicttoxml-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-dicttoxml = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-dicttoxml
Summary:        Converts a Python dictionary or other native data type into a valid XML string.
%description -n python3-dicttoxml

%prep
%global oreon_srcdir dicttoxml-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dicttoxml usr/lib/python3*/site-packages/dicttoxml* usr/lib64/python3*/site-packages/dicttoxml* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dicttoxml* usr/lib64/python3*/site-packages/dicttoxml* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dicttoxml -f %{oreon_filedir}/python3-dicttoxml.list

%changelog

%autochangelog
