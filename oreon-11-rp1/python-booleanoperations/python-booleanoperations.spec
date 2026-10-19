%global source0_hash 6d719f560d2a1dd676c812b844ecceb693c96791c76579089ab7d0f5db5cedbe
Name:           python-booleanoperations
Version:        0.10.0
Release:        1%{?dist}
Summary:        Boolean operations on paths.
License:        MIT
URL:            https://github.com/typemytype/booleanOperations
Source0:        https://files.pythonhosted.org/packages/source/b/booleanoperations/booleanoperations-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 30.3.0
Requires:       python3-booleanoperations = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-booleanoperations
Summary:        Boolean operations on paths.
%description -n python3-booleanoperations

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir booleanoperations-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-booleanoperations usr/lib/python3*/site-packages/booleanoperations* usr/lib64/python3*/site-packages/booleanoperations* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/booleanoperations* usr/lib64/python3*/site-packages/booleanoperations* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-booleanoperations -f %{oreon_filedir}/python3-booleanoperations.list

%changelog

%autochangelog
