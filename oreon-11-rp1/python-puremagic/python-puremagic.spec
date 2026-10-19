%global source0_hash eb4bddf07c177c4b434554b92165b67449f5a51e152b976202d6254498810eef
Name:           python-puremagic
Version:        2.2.0
Release:        1%{?dist}
Summary:        Pure python implementation of magic file detection
License:        MIT
URL:            https://github.com/cdgriffith/puremagic
Source0:        https://files.pythonhosted.org/packages/source/p/puremagic/puremagic-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-puremagic = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-puremagic
Summary:        Pure python implementation of magic file detection
%description -n python3-puremagic

%prep
%global oreon_srcdir puremagic-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-puremagic usr/lib/python3*/site-packages/puremagic* usr/lib64/python3*/site-packages/puremagic* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/puremagic* usr/lib64/python3*/site-packages/puremagic* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-puremagic -f %{oreon_filedir}/python3-puremagic.list

%changelog

%autochangelog
