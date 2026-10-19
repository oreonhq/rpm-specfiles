%global source0_hash 7c7e1a961a0b2f2472c1ac5b69affa0ae1132c39adcb67aba98568702b9cc23f
Name:           python-tomli
Version:        2.4.1
Release:        1%{?dist}
Summary:        A lil_ TOML parser
License:        MIT
URL:            https://github.com/hukkin/tomli
Source0:        https://files.pythonhosted.org/packages/source/t/tomli/tomli-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.12
Requires:       python3-tomli = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tomli
Summary:        A lil_ TOML parser
%description -n python3-tomli

%prep
%global oreon_srcdir tomli-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tomli usr/lib/python3*/site-packages/tomli* usr/lib64/python3*/site-packages/tomli* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tomli* usr/lib64/python3*/site-packages/tomli* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tomli -f %{oreon_filedir}/python3-tomli.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.0-1
- Prepare for Oreon 11 (RP1)
