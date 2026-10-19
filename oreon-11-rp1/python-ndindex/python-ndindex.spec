%global source0_hash 0f6113c1f031248f8818cbee1aa92aa3c9472b7701debcce9fddebcd2f610f11
Name:           python-ndindex
Version:        1.10.1
Release:        1%{?dist}
Summary:        A Python library for manipulating indices of ndarrays.
License:        MIT
URL:            https://quansight-labs.github.io/ndindex/
Source0:        https://files.pythonhosted.org/packages/source/n/ndindex/ndindex-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 72.2
Requires:       python3-ndindex = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ndindex
Summary:        A Python library for manipulating indices of ndarrays.
%description -n python3-ndindex

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ndindex-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ndindex usr/lib/python3*/site-packages/ndindex* usr/lib64/python3*/site-packages/ndindex* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ndindex* usr/lib64/python3*/site-packages/ndindex* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ndindex -f %{oreon_filedir}/python3-ndindex.list

%changelog

%autochangelog
