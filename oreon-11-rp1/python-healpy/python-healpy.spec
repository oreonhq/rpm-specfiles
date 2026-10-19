%global source0_hash 03b0e1551ae235c7290e9bfdf69fa9cdc194f8a2be51198c1924b15d826102ed
Name:           python-healpy
Version:        1.20.0
Release:        1%{?dist}
Summary:        Healpix tools package for Python
License:        GPL-2.0-only
URL:            https://github.com/healpy/healpy
Source0:        https://files.pythonhosted.org/packages/source/h/healpy/healpy-%{version}.tar.gz
Patch:          pykg-config_requirements.patch
Patch:          no_pytest-cython_doctests.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.16
BuildRequires:  python3dist(numpy) >= 2.0.0
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm) >= 8.0
Requires:       python3-healpy = %{version}-%{release}
# /oreon:deps
%package -n       python3-healpy+all
Summary:        Metapackage for python3-healpy all extras
Requires:       python3-healpy = %{version}-%{release}
Provides:       python3dist(healpy[all]) = %{version}-%{release}

%description -n python3-healpy+all
Metapackage for python3-healpy all extras.

%package -n       python3-healpy+test
Summary:        Metapackage for python3-healpy test extras
Requires:       python3-healpy = %{version}-%{release}
Provides:       python3dist(healpy[test]) = %{version}-%{release}

%description -n python3-healpy+test
Metapackage for python3-healpy test extras.

%package -n       python3-healpy+doc
Summary:        Metapackage for python3-healpy doc extras
Requires:       python3-healpy = %{version}-%{release}
Requires:       python3dist(sphinx) >= 6
Requires:       python3dist(sphinx) < 9
Provides:       python3dist(healpy[doc]) = %{version}-%{release}

%description -n python3-healpy+doc
Metapackage for python3-healpy doc extras.

%description

%package -n     python3-healpy
Summary:        Healpix tools package for Python
# oreon:reqs
Requires:       python3dist(numpy) >= 2.0.0
# /oreon:reqs
%description -n python3-healpy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir healpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-healpy usr/lib/python3*/site-packages/healpy* usr/lib64/python3*/site-packages/healpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/healpy* usr/lib64/python3*/site-packages/healpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-healpy -f %{oreon_filedir}/python3-healpy.list

%changelog

%autochangelog
