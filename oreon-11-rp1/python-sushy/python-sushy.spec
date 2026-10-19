%global source0_hash fc73170ad7506f301bb3beabcaa259814bff4547b26f0531bd56c63965dbaac8
Name:           python-sushy
Version:        5.13.0
Release:        1%{?dist}
Summary:        Sushy is a small Python library to communicate with Redfish based systems
License:        ...
URL:            https://docs.openstack.org/sushy/latest/
Source0:        https://files.pythonhosted.org/packages/source/s/sushy/sushy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.0.0
BuildRequires:  python3dist(setuptools) >= 64.0.0
Requires:       python3-sushy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sushy
Summary:        Sushy is a small Python library to communicate with Redfish based systems
%description -n python3-sushy

%prep
%global oreon_srcdir sushy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sushy usr/lib/python3*/site-packages/sushy* usr/lib64/python3*/site-packages/sushy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sushy* usr/lib64/python3*/site-packages/sushy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sushy -f %{oreon_filedir}/python3-sushy.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.2.0-7
- Prepare for Oreon 11 (RP1)
