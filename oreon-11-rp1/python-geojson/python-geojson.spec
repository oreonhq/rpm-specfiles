%global source0_hash 92e83b9cb378a450b42f1207bb9b2a031f9fc89185f335153c44369b8b8b71fd
Name:           python-geojson
Version:        3.3.0
Release:        1%{?dist}
Summary:        Python bindings and utilities for GeoJSON
License:        ...
URL:            https://github.com/jazzband/geojson
Source0:        https://files.pythonhosted.org/packages/source/g/geojson/geojson-%{version}.tar.gz
BuildArch:      noarch
Patch0:     remove-check.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-geojson = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-geojson
Summary:        Python bindings and utilities for GeoJSON
%description -n python3-geojson

%prep
%global oreon_srcdir geojson-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-geojson usr/lib/python3*/site-packages/geojson* usr/lib64/python3*/site-packages/geojson* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/geojson* usr/lib64/python3*/site-packages/geojson* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-geojson -f %{oreon_filedir}/python3-geojson.list

%changelog

%autochangelog
