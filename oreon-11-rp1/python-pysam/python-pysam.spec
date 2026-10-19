%global source0_hash 90f612afccdb454d2447ecb5229266c6e7f991093deed4ed0a791db01f7fc994
Name:           python-pysam
Version:        0.24.1
Release:        1%{?dist}
Summary:        Package for reading, manipulating, and writing genomic data
License:        ...
URL:            https://pysam.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/p/pysam/pysam-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) < 4
BuildRequires:  python3dist(cython) >= 3
BuildRequires:  python3dist(setuptools) >= 59.0
Requires:       python3-pysam = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pysam
Summary:        Package for reading, manipulating, and writing genomic data
%description -n python3-pysam

%prep
%global oreon_srcdir pysam-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pysam usr/lib/python3*/site-packages/pysam* usr/lib64/python3*/site-packages/pysam* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pysam* usr/lib64/python3*/site-packages/pysam* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pysam -f %{oreon_filedir}/python3-pysam.list

%changelog

%autochangelog
