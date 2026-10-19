%global source0_hash 25dfe7fd0152ccf292cb190d1928a47d588899c20b046854293e039e1c93e5e0
%bcond pens 0
Name:           python-defcon
Version:        0.12.2
Release:        1%{?dist}
Summary:        A set of flexible objects for representing UFO data
License:        MIT
URL:            https://github.com/robotools/defcon
Source0:        https://files.pythonhosted.org/packages/source/d/defcon/defcon-%{version}.tar.gz
Patch:          defcon-0.12.2-fonttools-4.60.0.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4
Requires:       python3-defcon = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-defcon
Summary:        A set of flexible objects for representing UFO data
%description -n python3-defcon

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-defcon usr/lib/python3*/site-packages/defcon* usr/lib64/python3*/site-packages/defcon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/defcon* usr/lib64/python3*/site-packages/defcon* usr/bin/*

%check

%pytest
%files
%files -n python3-defcon -f %{oreon_filedir}/python3-defcon.list

%changelog

%autochangelog
