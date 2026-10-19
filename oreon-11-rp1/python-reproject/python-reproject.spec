%global source0_hash 01ede715a1993c29431f52ff74189ef30f5e7b2e8b4dc88c1b002145a971dc1c
Name:           python-reproject
Version:        0.21.0
Release:        1%{?dist}
Summary:        Reproject astronomical images
License:        ...
URL:            https://reproject.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/r/reproject/reproject-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(extension-helpers) < 2
BuildRequires:  python3dist(extension-helpers) >= 1.4
BuildRequires:  python3dist(numpy) >= 2
Requires:       python3-reproject = %{version}-%{release}
# /oreon:deps
%package -n       python3-reproject+all
Summary:        Metapackage for python3-reproject all extras
Requires:       python3-reproject = %{version}-%{release}
Provides:       python3dist(reproject[all]) = %{version}-%{release}

%description -n python3-reproject+all
Metapackage for python3-reproject all extras.

%package -n       python3-reproject+test
Summary:        Metapackage for python3-reproject test extras
Requires:       python3-reproject = %{version}-%{release}
Provides:       python3dist(reproject[test]) = %{version}-%{release}

%description -n python3-reproject+test
Metapackage for python3-reproject test extras.

%package -n       python3-reproject+testall
Summary:        Metapackage for python3-reproject testall extras
Requires:       python3-reproject = %{version}-%{release}
Requires:       python3dist(shapely) >= 2.0.2
Requires:       python3dist(sunpy[map]) >= 6.0.1
Provides:       python3dist(reproject[testall]) = %{version}-%{release}

%description -n python3-reproject+testall
Metapackage for python3-reproject testall extras.

%package -n       python3-reproject+docs
Summary:        Metapackage for python3-reproject docs extras
Requires:       python3-reproject = %{version}-%{release}
Requires:       python3dist(sphinx-astropy[confv3]) >= 1.11
Provides:       python3dist(reproject[docs]) = %{version}-%{release}

%description -n python3-reproject+docs
Metapackage for python3-reproject docs extras.

%description

%package -n     python3-reproject
Summary:        Reproject astronomical images
# oreon:reqs
Requires:       python3dist(astropy) >= 5.0
Requires:       python3dist(astropy-healpix) >= 1.0
Requires:       python3dist(dask-image) >= 2025.11.0
Requires:       python3dist(dask[array]) >= 2024.4.1
Requires:       python3dist(fsspec) >= 2021.9
Requires:       python3dist(numpy) >= 1.23
Requires:       python3dist(pillow) >= 10.0
Requires:       python3dist(pyavm) >= 0.9.6
Requires:       python3dist(scipy) >= 1.9
Requires:       python3dist(zarr) >= 2.17.0
# /oreon:reqs
%description -n python3-reproject

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir reproject-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-reproject usr/lib/python3*/site-packages/reproject* usr/lib64/python3*/site-packages/reproject* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/reproject* usr/lib64/python3*/site-packages/reproject* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-reproject -f %{oreon_filedir}/python3-reproject.list

%changelog

%autochangelog
