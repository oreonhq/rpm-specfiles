%global source0_hash c1b6ae15f4ccad704f1fe8417da5c2250145c7bcdb91acb53833bf5aefdd9e48
Name:           python-rasterio
Version:        1.5.1
Release:        1%{?dist}
Summary:        Fast and direct raster I/O for use with NumPy
License:        BSD-3-Clause
URL:            https://github.com/rasterio/rasterio
Source0:        https://files.pythonhosted.org/packages/source/r/rasterio/rasterio-%{version}.tar.gz
Patch:          0001-Loosen-up-build-requirements.patch
Patch:          0002-xfail-warp-tests-gdal-3.12.2.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) <= 3.2
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(numpy) < 3
BuildRequires:  python3dist(numpy) >= 2
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-rasterio = %{version}-%{release}
# /oreon:deps
%package -n       python3-rasterio+all
Summary:        Metapackage for python3-rasterio all extras
Requires:       python3-rasterio = %{version}-%{release}
Provides:       python3dist(rasterio[all]) = %{version}-%{release}

%description -n python3-rasterio+all
Metapackage for python3-rasterio all extras.

%package -n       python3-rasterio+docs
Summary:        Metapackage for python3-rasterio docs extras
Requires:       python3-rasterio = %{version}-%{release}
Provides:       python3dist(rasterio[docs]) = %{version}-%{release}

%description -n python3-rasterio+docs
Metapackage for python3-rasterio docs extras.

%package -n       python3-rasterio+ipython
Summary:        Metapackage for python3-rasterio ipython extras
Requires:       python3-rasterio = %{version}-%{release}
Requires:       python3dist(ipython) >= 2.0
Provides:       python3dist(rasterio[ipython]) = %{version}-%{release}

%description -n python3-rasterio+ipython
Metapackage for python3-rasterio ipython extras.

%package -n       python3-rasterio+plot
Summary:        Metapackage for python3-rasterio plot extras
Requires:       python3-rasterio = %{version}-%{release}
Provides:       python3dist(rasterio[plot]) = %{version}-%{release}

%description -n python3-rasterio+plot
Metapackage for python3-rasterio plot extras.

%package -n       python3-rasterio+s3
Summary:        Metapackage for python3-rasterio s3 extras
Requires:       python3-rasterio = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.2.4
Provides:       python3dist(rasterio[s3]) = %{version}-%{release}

%description -n python3-rasterio+s3
Metapackage for python3-rasterio s3 extras.

%package -n       python3-rasterio+test
Summary:        Metapackage for python3-rasterio test extras
Requires:       python3-rasterio = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.2.4
Requires:       python3dist(pytest-cov) >= 2.2.0
Requires:       python3dist(pytest) >= 2.8.2
Provides:       python3dist(rasterio[test]) = %{version}-%{release}

%description -n python3-rasterio+test
Metapackage for python3-rasterio test extras.

%description

%package -n     python3-rasterio
Summary:        Fast and direct raster I/O for use with NumPy
# oreon:reqs
Requires:       python3dist(click) >= 4.0
Requires:       python3dist(numpy) >= 2
Requires:       python3dist(pyparsing) >= 3.0
# /oreon:reqs
%description -n python3-rasterio

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rasterio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rasterio usr/lib/python3*/site-packages/rasterio* usr/lib64/python3*/site-packages/rasterio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rasterio* usr/lib64/python3*/site-packages/rasterio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rasterio -f %{oreon_filedir}/python3-rasterio.list

%changelog

%autochangelog
