%global source0_hash 5e1ca2be9433e1e1f9f6d477e1e6c8029755caceefb4e349048955e3cb825529
Name:           python-photutils
Version:        3.0.0
Release:        1%{?dist}
Summary:        An Astropy package for source detection and photometry
License:        BSD-3-Clause
URL:            https://github.com/astropy/photutils
Source0:        https://files.pythonhosted.org/packages/source/p/photutils/photutils-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) < 4
BuildRequires:  python3dist(cython) >= 3.1.2
BuildRequires:  python3dist(extension-helpers) < 2
BuildRequires:  python3dist(extension-helpers) >= 1.3
BuildRequires:  python3dist(numpy) >= 2.0
BuildRequires:  python3dist(setuptools) >= 77.0
BuildRequires:  python3dist(setuptools-scm) >= 8.1
Requires:       python3-photutils = %{version}-%{release}
# /oreon:deps
%package -n       python3-photutils+all
Summary:        Metapackage for python3-photutils all extras
Requires:       python3-photutils = %{version}-%{release}
Requires:       python3dist(bottleneck) >= 1.4
Requires:       python3dist(gwcs) >= 0.20
Requires:       python3dist(matplotlib) >= 3.9
Requires:       python3dist(rasterio) >= 1.4
Requires:       python3dist(regions) >= 0.9
Requires:       python3dist(scikit-image) >= 0.23
Requires:       python3dist(shapely) >= 2.0
Requires:       python3dist(tqdm) >= 4.66
Provides:       python3dist(photutils[all]) = %{version}-%{release}

%description -n python3-photutils+all
Metapackage for python3-photutils all extras.

%package -n       python3-photutils+test
Summary:        Metapackage for python3-photutils test extras
Requires:       python3-photutils = %{version}-%{release}
Requires:       python3dist(pytest-astropy) >= 0.11
Requires:       python3dist(pytest-xdist) >= 3.5
Requires:       python3dist(tox) >= 4.12
Provides:       python3dist(photutils[test]) = %{version}-%{release}

%description -n python3-photutils+test
Metapackage for python3-photutils test extras.

%package -n       python3-photutils+docs
Summary:        Metapackage for python3-photutils docs extras
Requires:       python3-photutils = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8.2
Requires:       python3dist(sphinx-astropy[confv2]) >= 1.9.1
Requires:       python3dist(sphinx-design) >= 0.6
Requires:       python3dist(sphinx-reredirects) >= 1.1
Provides:       python3dist(photutils[docs]) = %{version}-%{release}

%description -n python3-photutils+docs
Metapackage for python3-photutils docs extras.

%package -n       python3-photutils+dev
Summary:        Metapackage for python3-photutils dev extras
Requires:       python3-photutils = %{version}-%{release}
Requires:       python3dist(pre-commit) >= 4.0
Provides:       python3dist(photutils[dev]) = %{version}-%{release}

%description -n python3-photutils+dev
Metapackage for python3-photutils dev extras.

%description

%package -n     python3-photutils
Summary:        An Astropy package for source detection and photometry
# oreon:reqs
Requires:       python3dist(astropy) >= 6.1.4
Requires:       python3dist(numpy) >= 2.0
Requires:       python3dist(scipy) >= 1.13
# /oreon:reqs
%description -n python3-photutils

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir photutils-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-photutils usr/lib/python3*/site-packages/photutils* usr/lib64/python3*/site-packages/photutils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/photutils* usr/lib64/python3*/site-packages/photutils* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-photutils -f %{oreon_filedir}/python3-photutils.list

%changelog

%autochangelog
