%global source0_hash d341f228c5b5ccf3c473751f6c6f09d8d83c5da49846a6ee31eb60b65607e0ef
Name:           python-mockito
Version:        2.0.4
Release:        1%{?dist}
Summary:        Spying framework
License:        MIT
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/m/mockito/mockito-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mockito = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mockito
Summary:        Spying framework
%description -n python3-mockito

%prep
%global oreon_srcdir mockito-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mockito usr/lib/python3*/site-packages/mockito* usr/lib64/python3*/site-packages/mockito* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mockito* usr/lib64/python3*/site-packages/mockito* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mockito -f %{oreon_filedir}/python3-mockito.list

%changelog

%autochangelog
