%global source0_hash 579554887ffd189226774b87570f4a76db75cf0efcbaffcacd5e98b8ee877f61
Name:           python-cerberus
Version:        1.3.8
Release:        1%{?dist}
Summary:        Lightweight, extensible schema and data validation tool for Pythondictionaries.
License:        ISC
URL:            https://github.com/pyeve/cerberus
Source0:        https://files.pythonhosted.org/packages/source/c/cerberus/cerberus-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cerberus = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cerberus
Summary:        Lightweight, extensible schema and data validation tool for Pythondictionaries.
%description -n python3-cerberus

%prep
%global oreon_srcdir cerberus-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cerberus usr/lib/python3*/site-packages/cerberus* usr/lib64/python3*/site-packages/cerberus* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cerberus* usr/lib64/python3*/site-packages/cerberus* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cerberus -f %{oreon_filedir}/python3-cerberus.list

%changelog

%autochangelog
