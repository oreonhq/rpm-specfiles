%global source0_hash e478fb2a1391a56c8a6e10cc97c4a9002b410ecd1ac28c18d780661762e271bd
Name:           python-frozendict
Version:        2.4.7
Release:        1%{?dist}
Summary:        A simple immutable dictionary
License:        ...
URL:            https://github.com/Marco-Sulla/python-frozendict
Source0:        https://files.pythonhosted.org/packages/source/f/frozendict/frozendict-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-frozendict = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-frozendict
Summary:        A simple immutable dictionary
%description -n python3-frozendict

%prep
%global oreon_srcdir frozendict-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-frozendict usr/lib/python3*/site-packages/frozendict* usr/lib64/python3*/site-packages/frozendict* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/frozendict* usr/lib64/python3*/site-packages/frozendict* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-frozendict -f %{oreon_filedir}/python3-frozendict.list

%changelog

%autochangelog
