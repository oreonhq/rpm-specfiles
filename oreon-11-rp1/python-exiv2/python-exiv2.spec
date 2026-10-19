%global source0_hash b07031aeefe9248866a0fbf5a8270c7504abced116cf998537d3bc15f353909c
Name:           python-exiv2
Version:        0.19.2
Release:        1%{?dist}
Summary:        Python interface to libexiv2
License:        GPL-3.0-or-later
URL:            https://github.com/jim-easterbrook/python-exiv2
Source0:        https://files.pythonhosted.org/packages/source/e/exiv2/exiv2-%{version}.tar.gz
Patch:          https://github.com/jim-easterbrook/python-exiv2/commit/fe98ad09ff30f1b6cc5fd5dcc0769f9505c09166.patch
Patch:          https://github.com/jim-easterbrook/python-exiv2/commit/e0a5284620e8d020771bf8c1fa73d6113e662ebf.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 61.0
BuildRequires:  python3dist(setuptools) >= 59.6
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-exiv2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-exiv2
Summary:        Python interface to libexiv2
%description -n python3-exiv2

%prep
%global oreon_srcdir exiv2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-exiv2 usr/lib/python3*/site-packages/exiv2* usr/lib64/python3*/site-packages/exiv2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/exiv2* usr/lib64/python3*/site-packages/exiv2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-exiv2 -f %{oreon_filedir}/python3-exiv2.list

%changelog

%autochangelog
