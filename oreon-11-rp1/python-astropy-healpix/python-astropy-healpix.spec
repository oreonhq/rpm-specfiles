%global source0_hash 0e3f1c94064c45da779900cb90c938df7aef99a924abb23eeb893b16540e77e6
Name:           python-astropy-healpix
Version:        2.0.1
Release:        1%{?dist}
Summary:        BSD-licensed HEALPix for Astropy
License:        ...
URL:            https://github.com/astropy/astropy-healpix
Source0:        https://files.pythonhosted.org/packages/source/a/astropy_healpix/astropy_healpix-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(extension-helpers) < 2
BuildRequires:  python3dist(extension-helpers) >= 1.3
BuildRequires:  python3dist(numpy) >= 2.0.0
BuildRequires:  python3dist(setuptools) >= 77.0.1
Requires:       python3-astropy-healpix = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-astropy-healpix
Summary:        BSD-licensed HEALPix for Astropy
%description -n python3-astropy-healpix

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir astropy_healpix-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-astropy-healpix usr/lib/python3*/site-packages/astropy_healpix* usr/lib64/python3*/site-packages/astropy_healpix* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/astropy_healpix* usr/lib64/python3*/site-packages/astropy_healpix* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-astropy-healpix -f %{oreon_filedir}/python3-astropy-healpix.list

%changelog

%autochangelog
