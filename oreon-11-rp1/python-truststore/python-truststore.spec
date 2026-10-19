%global source0_hash 9d91bd436463ad5e4ee4aba766628dd6cd7010cf3e2461756b3303710eebc301
Name:           python-truststore
Version:        0.10.4
Release:        1%{?dist}
Summary:        Verify certificates using native system trust stores
License:        MIT
URL:            https://github.com/sethmlarson/truststore
Source0:        https://files.pythonhosted.org/packages/source/t/truststore/truststore-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-truststore = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-truststore
Summary:        Verify certificates using native system trust stores
%description -n python3-truststore

%prep
%global oreon_srcdir truststore-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-truststore usr/lib/python3*/site-packages/truststore* usr/lib64/python3*/site-packages/truststore* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/truststore* usr/lib64/python3*/site-packages/truststore* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-truststore -f %{oreon_filedir}/python3-truststore.list

%changelog

%autochangelog
