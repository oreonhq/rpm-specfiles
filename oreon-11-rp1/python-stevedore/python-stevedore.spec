%global source0_hash e97a2667923efda926e8713fde6a73616df68210a3cbc6f02b48967b676fd8bf
Name:           python-stevedore
Version:        5.9.1
Release:        1%{?dist}
Summary:        Manage dynamic plugins for Python applications
License:        Apache-2.0
URL:            https://docs.openstack.org/stevedore
Source0:        https://files.pythonhosted.org/packages/source/s/stevedore/stevedore-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-stevedore = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-stevedore
Summary:        Manage dynamic plugins for Python applications
%description -n python3-stevedore

%prep
%global oreon_srcdir stevedore-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-stevedore usr/lib/python3*/site-packages/stevedore* usr/lib64/python3*/site-packages/stevedore* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/stevedore* usr/lib64/python3*/site-packages/stevedore* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-stevedore -f %{oreon_filedir}/python3-stevedore.list

%changelog

%autochangelog
