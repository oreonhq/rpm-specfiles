%global source0_hash 53afa5b541942c8b32034703f20639691d45048da67926fdbef525df357ce0d0
Name:           python-openstackdocstheme
Version:        3.6.0
Release:        1%{?dist}
Summary:        OpenStack Docs Theme
License:        Apache-2.0
URL:            https://docs.openstack.org/openstackdocstheme
Source0:        https://files.pythonhosted.org/packages/source/o/openstackdocstheme/openstackdocstheme-%{version}.tar.gz
BuildArch:      noarch
Patch0001:      0001-Remove-all-Google-Analytics-tracking.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-openstackdocstheme = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-openstackdocstheme
Summary:        OpenStack Docs Theme
%description -n python3-openstackdocstheme

%prep
%global oreon_srcdir openstackdocstheme-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-openstackdocstheme usr/lib/python3*/site-packages/openstackdocstheme* usr/lib64/python3*/site-packages/openstackdocstheme* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openstackdocstheme* usr/lib64/python3*/site-packages/openstackdocstheme* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-openstackdocstheme -f %{oreon_filedir}/python3-openstackdocstheme.list

%changelog

%autochangelog
