%global source0_hash 2e5543bea424e60e9e42eef70bff597be48649d8f68ba061a7a092b2477d5464
Name:           python-pybtex
Version:        0.26.1
Release:        1%{?dist}
Summary:        A BibTeX-compatible bibliography processor in Python
License:        MIT
URL:            https://pybtex.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pybtex/pybtex-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pybtex = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pybtex
Summary:        A BibTeX-compatible bibliography processor in Python
%description -n python3-pybtex

%prep
%global oreon_srcdir pybtex-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pybtex usr/lib/python3*/site-packages/pybtex* usr/lib64/python3*/site-packages/pybtex* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pybtex* usr/lib64/python3*/site-packages/pybtex* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pybtex -f %{oreon_filedir}/python3-pybtex.list

%changelog

%autochangelog
