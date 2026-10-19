%global source0_hash 27b485b9161925924c1d8e78e66bb342e6e3bc49bf675d0a67b49bad9c291521
Name:           python-qtconsole
Version:        5.7.2
Release:        1%{?dist}
Summary:        Jupyter Qt console
License:        ...
URL:            http://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/q/qtconsole/qtconsole-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-qtconsole = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-qtconsole
Summary:        Jupyter Qt console
%description -n python3-qtconsole

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir qtconsole-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-qtconsole usr/lib/python3*/site-packages/qtconsole* usr/lib64/python3*/site-packages/qtconsole* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/qtconsole* usr/lib64/python3*/site-packages/qtconsole* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-qtconsole -f %{oreon_filedir}/python3-qtconsole.list

%changelog

%autochangelog
