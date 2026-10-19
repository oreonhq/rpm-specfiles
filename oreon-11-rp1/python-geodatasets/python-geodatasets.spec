%global source0_hash c55358e118af956605781ae4fe5dccf26c63dc89408b3298726d21b879c9b2b1
Name:           python-geodatasets
Version:        2026.5.1
Release:        1%{?dist}
Summary:        Spatial data examples
License:        ...
URL:            https://github.com/geopandas/geodatasets
Source0:        https://files.pythonhosted.org/packages/source/g/geodatasets/geodatasets-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-geodatasets = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-geodatasets
Summary:        Spatial data examples
%description -n python3-geodatasets

%prep
%global oreon_srcdir geodatasets-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-geodatasets usr/lib/python3*/site-packages/geodatasets* usr/lib64/python3*/site-packages/geodatasets* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/geodatasets* usr/lib64/python3*/site-packages/geodatasets* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-geodatasets -f %{oreon_filedir}/python3-geodatasets.list

%changelog

%autochangelog
