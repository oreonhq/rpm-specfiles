%global source0_hash e00372357a93a9028f75ea7343d867893bd8d4b89833de17b18438725929c885
Name:           python-contextily
Version:        1.7.1
Release:        1%{?dist}
Summary:        Context geo-tiles in Python
License:        BSD-3-Clause
URL:            https://github.com/geopandas/contextily
Source0:        https://files.pythonhosted.org/packages/source/c/contextily/contextily-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Mark-another-test-as-using-the-network.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-contextily = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-contextily
Summary:        Context geo-tiles in Python
%description -n python3-contextily

%prep
%global oreon_srcdir contextily-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-contextily usr/lib/python3*/site-packages/contextily* usr/lib64/python3*/site-packages/contextily* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/contextily* usr/lib64/python3*/site-packages/contextily* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-contextily -f %{oreon_filedir}/python3-contextily.list

%changelog

%autochangelog
