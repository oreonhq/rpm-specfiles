%global source0_hash 278a45608cf16e79c0ae10851d869185c6b78f86610df8f27a451a18c1fec732
Name:           python-debtcollector
Version:        3.1.0
Release:        1%{?dist}
Summary:        A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner.
License:        Apache-2.0
URL:            https://docs.openstack.org/debtcollector/
Source0:        https://files.pythonhosted.org/packages/source/d/debtcollector/debtcollector-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-debtcollector = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-debtcollector
Summary:        A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner.
%description -n python3-debtcollector

%prep
%global oreon_srcdir debtcollector-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-debtcollector usr/lib/python3*/site-packages/debtcollector* usr/lib64/python3*/site-packages/debtcollector* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/debtcollector* usr/lib64/python3*/site-packages/debtcollector* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-debtcollector -f %{oreon_filedir}/python3-debtcollector.list

%changelog

%autochangelog
