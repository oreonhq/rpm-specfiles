%global source0_hash f02e4021397ae02a139defdc6813b9942ab163de90affddd4ce4efbac299f619
Name:           python-pyroaring
Version:        1.1.0
Release:        1%{?dist}
Summary:        Library for handling efficiently sorted integer sets.
License:        MIT
URL:            https://github.com/Ezibenroc/PyRoaringBitMap
Source0:        https://files.pythonhosted.org/packages/source/p/pyroaring/pyroaring-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyroaring = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyroaring
Summary:        Library for handling efficiently sorted integer sets.
%description -n python3-pyroaring

%prep
%global oreon_srcdir pyroaring-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyroaring usr/lib/python3*/site-packages/pyroaring* usr/lib64/python3*/site-packages/pyroaring* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyroaring* usr/lib64/python3*/site-packages/pyroaring* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyroaring -f %{oreon_filedir}/python3-pyroaring.list

%changelog

%autochangelog
