%global source0_hash 40a20f1292cafb29b095139abd07c0cbf2da09b91b6573512e86054503914677
Name:           python-pyshtools
Version:        4.14.1
Release:        1%{?dist}
Summary:        SHTOOLS - Spherical Harmonic Tools
License:        BSD-3-Clause
URL:            https://shtools.github.io/SHTOOLS/
Source0:        https://files.pythonhosted.org/packages/source/p/pyshtools/pyshtools-%{version}.tar.gz
Patch:          0001-Use-normal-numpy-as-build-dependency.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(meson-python) >= 0.14
BuildRequires:  python3dist(numpy) >= 2.0.0
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-pyshtools = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyshtools+cartopy
Summary:        Metapackage for python3-pyshtools cartopy extras
Requires:       python3-pyshtools = %{version}-%{release}
Requires:       python3dist(cartopy) >= 0.18.0
Provides:       python3dist(pyshtools[cartopy]) = %{version}-%{release}

%description -n python3-pyshtools+cartopy
Metapackage for python3-pyshtools cartopy extras.

%package -n       python3-pyshtools+pygmt
Summary:        Metapackage for python3-pyshtools pygmt extras
Requires:       python3-pyshtools = %{version}-%{release}
Requires:       python3dist(pygmt) >= 0.7
Provides:       python3dist(pyshtools[pygmt]) = %{version}-%{release}

%description -n python3-pyshtools+pygmt
Metapackage for python3-pyshtools pygmt extras.

%package -n       python3-pyshtools+palettable
Summary:        Metapackage for python3-pyshtools palettable extras
Requires:       python3-pyshtools = %{version}-%{release}
Requires:       python3dist(palettable) >= 3.3
Provides:       python3dist(pyshtools[palettable]) = %{version}-%{release}

%description -n python3-pyshtools+palettable
Metapackage for python3-pyshtools palettable extras.

%package -n       python3-pyshtools+ducc
Summary:        Metapackage for python3-pyshtools ducc extras
Requires:       python3-pyshtools = %{version}-%{release}
Requires:       python3dist(ducc0) >= 0.15
Provides:       python3dist(pyshtools[ducc]) = %{version}-%{release}

%description -n python3-pyshtools+ducc
Metapackage for python3-pyshtools ducc extras.

%description

%package -n     python3-pyshtools
Summary:        SHTOOLS - Spherical Harmonic Tools
# oreon:reqs
Requires:       python3dist(astropy) >= 4.0
Requires:       python3dist(boule) >= 0.5.0
Requires:       python3dist(matplotlib) >= 3.3
Requires:       python3dist(numpy) >= 1.23.5
Requires:       python3dist(pooch) >= 1.1
Requires:       python3dist(scipy) >= 0.14.0
# /oreon:reqs
%description -n python3-pyshtools

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyshtools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyshtools usr/lib/python3*/site-packages/pyshtools* usr/lib64/python3*/site-packages/pyshtools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyshtools* usr/lib64/python3*/site-packages/pyshtools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyshtools -f %{oreon_filedir}/python3-pyshtools.list

%changelog

%autochangelog
