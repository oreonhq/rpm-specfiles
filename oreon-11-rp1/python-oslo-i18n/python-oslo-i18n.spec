%global source0_hash 574bcf21873b185068bcec951de1ec093158ffdff05a8055fd18ddcb69f69e65
Name:           python-oslo-i18n
Version:        6.9.0
Release:        1%{?dist}
Summary:        Oslo i18n library
License:        Apache-2.0
URL:            https://docs.openstack.org/oslo.i18n
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_i18n/oslo_i18n-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-oslo-i18n = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-oslo-i18n
Summary:        Oslo i18n library
%description -n python3-oslo-i18n

%prep
%global oreon_srcdir oslo_i18n-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oslo-i18n usr/lib/python3*/site-packages/oslo_i18n* usr/lib64/python3*/site-packages/oslo_i18n* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oslo_i18n* usr/lib64/python3*/site-packages/oslo_i18n* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oslo-i18n -f %{oreon_filedir}/python3-oslo-i18n.list

%changelog

%autochangelog
