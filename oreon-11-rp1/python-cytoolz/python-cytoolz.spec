%global source0_hash 13a7bf254c3c0d28b12e2290b82aed0f0977a4c2a2bf84854fcdc7796a29f3b0
Name:           python-cytoolz
Version:        1.1.0
Release:        1%{?dist}
Summary:        Cython implementation of Toolz: High performance functional utilities
License:        BSD-3-Clause
URL:            https://github.com/pytoolz/cytoolz
Source0:        https://files.pythonhosted.org/packages/source/c/cytoolz/cytoolz-%{version}.tar.gz
Patch:          python-cytoolz-0001-Test-against-Python-3.14-dev-on-CI-592.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.29
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-git-versioning) >= 2.0
Requires:       python3-cytoolz = %{version}-%{release}
# /oreon:deps
%package -n       python3-cytoolz+cython
Summary:        Metapackage for python3-cytoolz cython extras
Requires:       python3-cytoolz = %{version}-%{release}
Requires:       python3dist(cython) >= 0.29
Provides:       python3dist(cytoolz[cython]) = %{version}-%{release}

%description -n python3-cytoolz+cython
Metapackage for python3-cytoolz cython extras.

%package -n       python3-cytoolz+test
Summary:        Metapackage for python3-cytoolz test extras
Requires:       python3-cytoolz = %{version}-%{release}
Provides:       python3dist(cytoolz[test]) = %{version}-%{release}

%description -n python3-cytoolz+test
Metapackage for python3-cytoolz test extras.

%description

%package -n     python3-cytoolz
Summary:        Cython implementation of Toolz: High performance functional utilities
# oreon:reqs
Requires:       python3dist(toolz) >= 0.8.0
# /oreon:reqs
%description -n python3-cytoolz

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cytoolz-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cytoolz usr/lib/python3*/site-packages/cytoolz* usr/lib64/python3*/site-packages/cytoolz* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cytoolz* usr/lib64/python3*/site-packages/cytoolz* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cytoolz -f %{oreon_filedir}/python3-cytoolz.list

%changelog

%autochangelog
