%global source0_hash 095a980a1976adff48c3de1f73d75efe9b39da7214dc7c891a2363240716a9e7
Name:           python-minikerberos
Version:        0.4.9
Release:        1%{?dist}
Summary:        Kerberos manipulation library in pure Python
License:        MIT
URL:            https://github.com/skelsec/minikerberos
Source0:        https://files.pythonhosted.org/packages/source/m/minikerberos/minikerberos-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-minikerberos = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-minikerberos
Summary:        Kerberos manipulation library in pure Python
%description -n python3-minikerberos

%prep
%global oreon_srcdir minikerberos-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-minikerberos usr/lib/python3*/site-packages/minikerberos* usr/lib64/python3*/site-packages/minikerberos* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/minikerberos* usr/lib64/python3*/site-packages/minikerberos* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-minikerberos -f %{oreon_filedir}/python3-minikerberos.list

%changelog

%autochangelog
