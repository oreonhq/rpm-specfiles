%global source0_hash 45c18ff2b7c90163dfdff7e20d3f482514cc7aac26bc2547744e79dfa761e458
Name:           python-textfsm
Version:        2.1.0
Release:        1%{?dist}
Summary:        Python module for parsing semi-structured text into python tables.
License:        ...
URL:            https://github.com/google/textfsm
Source0:        https://files.pythonhosted.org/packages/source/t/textfsm/textfsm-%{version}.tar.gz
BuildArch:      noarch
Patch:          textfsm-1.1.3-no-future.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-textfsm = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-textfsm
Summary:        Python module for parsing semi-structured text into python tables.
%description -n python3-textfsm

%prep
%global oreon_srcdir textfsm-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-textfsm usr/lib/python3*/site-packages/textfsm* usr/lib64/python3*/site-packages/textfsm* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/textfsm* usr/lib64/python3*/site-packages/textfsm* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-textfsm -f %{oreon_filedir}/python3-textfsm.list

%changelog

%autochangelog
