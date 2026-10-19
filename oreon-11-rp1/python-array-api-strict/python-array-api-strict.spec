%global source0_hash 27485fd687c678894fb193e8f9f5116651a0bfc19dccea164d7d5df83b4e9a82
Name:           python-array-api-strict
Version:        2.6.1
Release:        1%{?dist}
Summary:        A strict, minimal implementation of the Python array API standard.
License:        ...
URL:            https://data-apis.org/array-api-strict/
Source0:        https://files.pythonhosted.org/packages/source/a/array_api_strict/array_api_strict-%{version}.tar.gz
BuildArch:      noarch
Patch:          Fix-test_iter-with-Python-3.14-beta-1.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) <= 75
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(setuptools-scm) < 10
BuildRequires:  python3dist(setuptools-scm) > 8
Requires:       python3-array-api-strict = %{version}-%{release}
# /oreon:deps
%package -n       python3-array-api-strict+test
Summary:        Metapackage for python3-array-api-strict test extras
Requires:       python3-array-api-strict = %{version}-%{release}
Provides:       python3dist(array-api-strict[test]) = %{version}-%{release}

%description -n python3-array-api-strict+test
Metapackage for python3-array-api-strict test extras.

%description

%package -n     python3-array-api-strict
Summary:        A strict, minimal implementation of the Python array API standard.
%description -n python3-array-api-strict

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir array_api_strict-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-array-api-strict usr/lib/python3*/site-packages/array_api_strict* usr/lib64/python3*/site-packages/array_api_strict* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/array_api_strict* usr/lib64/python3*/site-packages/array_api_strict* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-array-api-strict -f %{oreon_filedir}/python3-array-api-strict.list

%changelog

%autochangelog
