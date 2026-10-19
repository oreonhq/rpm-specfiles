%global source0_hash 7e1fb03c6a97167959f37d930300154e0ee837ecdb85798c2bbe8878b56caaaf
Name:           python-oslo-context
Version:        6.5.0
Release:        1%{?dist}
Summary:        Oslo Context library
License:        Apache-2.0
URL:            https://docs.openstack.org/oslo.context
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_context/oslo_context-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-oslo-context = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-oslo-context
Summary:        Oslo Context library
%description -n python3-oslo-context

%prep
%global oreon_srcdir oslo_context-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oslo-context usr/lib/python3*/site-packages/oslo_context* usr/lib64/python3*/site-packages/oslo_context* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oslo_context* usr/lib64/python3*/site-packages/oslo_context* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oslo-context -f %{oreon_filedir}/python3-oslo-context.list

%changelog

%autochangelog
