%global source0_hash 1bd4321cc63c06954953eae9eb8fb5d9075296b96c0e3ed34ccb91a0dcce31a5
Name:           python-pymongo
Version:        4.18.2
Release:        1%{?dist}
Summary:        PyMongo - the Official MongoDB Python driver
License:        Apache-2.0
URL:            https://www.mongodb.org
Source0:        https://files.pythonhosted.org/packages/source/p/pymongo/pymongo-%{version}.tar.gz
Patch0:         pymongo-nonfatal-warnings.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-requirements-txt) >= 0.4.1
BuildRequires:  python3dist(hatchling) > 1.24
BuildRequires:  python3dist(setuptools) >= 65.0
Requires:       python3-pymongo = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pymongo
Summary:        PyMongo - the Official MongoDB Python driver
%description -n python3-pymongo

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pymongo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pymongo usr/lib/python3*/site-packages/pymongo* usr/lib64/python3*/site-packages/pymongo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pymongo* usr/lib64/python3*/site-packages/pymongo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pymongo -f %{oreon_filedir}/python3-pymongo.list

%changelog

%autochangelog
