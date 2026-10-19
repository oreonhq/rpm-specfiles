%global source0_hash e1b3c38c5d4d3ef5024a182a6d1bf1e0c51ab221825781c741aeb4d0c079a7e2
Name:           python-affine
Version:        3.0.1
Release:        1%{?dist}
Summary:        Matrices describing affine transformation of the plane
License:        BSD-3-Clause
URL:            https://github.com/rasterio/affine
Source0:        https://files.pythonhosted.org/packages/source/a/affine/affine-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-affine = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-affine
Summary:        Matrices describing affine transformation of the plane
# oreon:reqs
Requires:       python3dist(attrs) >= 21.3.0
# /oreon:reqs
%description -n python3-affine

%prep
%global oreon_srcdir affine-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-affine usr/lib/python3*/site-packages/affine* usr/lib64/python3*/site-packages/affine* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/affine* usr/lib64/python3*/site-packages/affine* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-affine -f %{oreon_filedir}/python3-affine.list

%changelog

%autochangelog
