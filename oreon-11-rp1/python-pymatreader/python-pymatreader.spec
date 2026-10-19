%global source0_hash 19c38ef7e174f1e53f48a2433c92bf0342df56c35df32ec025c05552027cd039
Name:           python-pymatreader
Version:        1.3.1
Release:        1%{?dist}
Summary:        Convenient reader for Matlab mat files
License:        BSD-2-Clause
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/p/pymatreader/pymatreader-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pymatreader = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pymatreader
Summary:        Convenient reader for Matlab mat files
# oreon:reqs
Requires:       python3dist(h5py) >= 3.7
Requires:       python3dist(numpy) >= 1.21.3
Requires:       python3dist(scipy) >= 1.11
Requires:       python3dist(xmltodict) > 0.13
# /oreon:reqs
%description -n python3-pymatreader

%prep
%global oreon_srcdir pymatreader-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pymatreader usr/lib/python3*/site-packages/pymatreader* usr/lib64/python3*/site-packages/pymatreader* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pymatreader* usr/lib64/python3*/site-packages/pymatreader* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pymatreader -f %{oreon_filedir}/python3-pymatreader.list

%changelog

%autochangelog
