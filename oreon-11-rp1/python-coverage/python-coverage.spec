%global source0_hash ca64d9f1f384f151b9511bec01126072acd2f313439f8ed015a22d8790aab6fa
Name:           python-coverage
Version:        7.16.2
Release:        1%{?dist}
Summary:        Code coverage measurement for Python
License:        Apache-2.0
URL:            https://coverage.readthedocs.io/en/7.16.1
Source0:        https://files.pythonhosted.org/packages/source/c/coverage/coverage-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-coverage = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-coverage
Summary:        Code coverage measurement for Python
%description -n python3-coverage

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir coverage-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-coverage usr/lib/python3*/site-packages/coverage* usr/lib64/python3*/site-packages/coverage* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/coverage* usr/lib64/python3*/site-packages/coverage* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-coverage -f %{oreon_filedir}/python3-coverage.list

%changelog

%autochangelog
