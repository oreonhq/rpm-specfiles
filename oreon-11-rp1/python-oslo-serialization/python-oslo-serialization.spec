%global source0_hash 8326e85a80856c1068007423fcf6fe29dd2fe57a32f5d87fff0120b555b4b67c
Name:           python-oslo-serialization
Version:        5.11.0
Release:        1%{?dist}
Summary:        Oslo Serialization library
License:        Apache-2.0
URL:            https://docs.openstack.org/oslo.serialization
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_serialization/oslo_serialization-%{version}.tar.gz
BuildArch:      noarch
Patch0001:        0001-Remove-extra-spaces-in-tox.ini.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-oslo-serialization = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-oslo-serialization
Summary:        Oslo Serialization library
%description -n python3-oslo-serialization

%prep
%global oreon_srcdir oslo_serialization-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oslo-serialization usr/lib/python3*/site-packages/oslo_serialization* usr/lib64/python3*/site-packages/oslo_serialization* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oslo_serialization* usr/lib64/python3*/site-packages/oslo_serialization* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oslo-serialization -f %{oreon_filedir}/python3-oslo-serialization.list

%changelog

%autochangelog
