%global source0_hash dc32a556b3ad31ae79813bb9e7ba60a23469760acee69119dcbfbd80aa16f728
Name:           python-pyopnsense
Version:        0.4.0
Release:        1%{?dist}
Summary:        A python API client for OPNsense
License:        ...
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/p/pyopnsense/pyopnsense-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-opnsense-rm-python-mock-usage.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyopnsense = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyopnsense
Summary:        A python API client for OPNsense
%description -n python3-pyopnsense

%prep
%global oreon_srcdir pyopnsense-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyopnsense usr/lib/python3*/site-packages/pyopnsense* usr/lib64/python3*/site-packages/pyopnsense* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyopnsense* usr/lib64/python3*/site-packages/pyopnsense* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyopnsense -f %{oreon_filedir}/python3-pyopnsense.list

%changelog

%autochangelog
