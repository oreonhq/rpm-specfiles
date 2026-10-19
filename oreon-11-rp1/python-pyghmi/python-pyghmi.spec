%global source0_hash 30a0b2e145a3e4329c8d86948635eee3b3479ec6a7ecbc4cc3507e6df3fe59c2
Name:           python-pyghmi
Version:        1.6.19
Release:        1%{?dist}
Summary:        Python General Hardware Management Initiative _IPMI and others_
License:        ...
URL:            http://github.com/openstack/pyghmi/
Source0:        https://files.pythonhosted.org/packages/source/p/pyghmi/pyghmi-%{version}.tar.gz
BuildArch:      noarch
Patch1000:  nopbr.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyghmi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyghmi
Summary:        Python General Hardware Management Initiative _IPMI and others_
%description -n python3-pyghmi

%prep
%global oreon_srcdir pyghmi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyghmi usr/lib/python3*/site-packages/pyghmi* usr/lib64/python3*/site-packages/pyghmi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyghmi* usr/lib64/python3*/site-packages/pyghmi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyghmi -f %{oreon_filedir}/python3-pyghmi.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{?version:%{version}}%{!?version:1.6.2}-5
- Prepare for Oreon 11 (RP1)
