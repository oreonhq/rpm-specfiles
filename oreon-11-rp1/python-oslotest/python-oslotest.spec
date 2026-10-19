%global source0_hash 5ce97347734f08ca626bb496962a8bc7adbae9693730f5859d9c5293d4a2fd80
Name:           python-oslotest
Version:        6.1.1
Release:        1%{?dist}
Summary:        Oslo test framework
License:        ...
URL:            https://docs.openstack.org/oslotest
Source0:        https://files.pythonhosted.org/packages/source/o/oslotest/oslotest-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-oslotest = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-oslotest
Summary:        Oslo test framework
%description -n python3-oslotest

%prep
%global oreon_srcdir oslotest-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oslotest usr/lib/python3*/site-packages/oslotest* usr/lib64/python3*/site-packages/oslotest* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oslotest* usr/lib64/python3*/site-packages/oslotest* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oslotest -f %{oreon_filedir}/python3-oslotest.list

%changelog

%autochangelog
