%global source0_hash 361b495928fdbf5b58d0969bb6775339019da5e93ca74d61ddf4eb5edd6ce604
Name:           python-xarray
Version:        2026.7.0
Release:        1%{?dist}
Summary:        N-D labeled arrays and datasets in Python
License:        Apache-2.0
URL:            https://xarray.dev/
Source0:        https://files.pythonhosted.org/packages/source/x/xarray/xarray-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-xarray = %{version}-%{release}
# /oreon:deps
%package -n       python3-xarray+accel
Summary:        Metapackage for python3-xarray accel extras
Requires:       python3-xarray = %{version}-%{release}
Requires:       python3dist(scipy) >= 1.15
Requires:       python3dist(numbagg) >= 0.9
Requires:       python3dist(numba) >= 0.62
Requires:       python3dist(flox) >= 0.10
Provides:       python3dist(xarray[accel]) = %{version}-%{release}

%description -n python3-xarray+accel
Metapackage for python3-xarray accel extras.

%package -n       python3-xarray+complete
Summary:        Metapackage for python3-xarray complete extras
Requires:       python3-xarray = %{version}-%{release}
Provides:       python3dist(xarray[complete]) = %{version}-%{release}

%description -n python3-xarray+complete
Metapackage for python3-xarray complete extras.

%package -n       python3-xarray+io
Summary:        Metapackage for python3-xarray io extras
Requires:       python3-xarray = %{version}-%{release}
Requires:       python3dist(netcdf4) >= 1.6.0
Requires:       python3dist(h5netcdf[h5py]) >= 1.5.0
Requires:       python3dist(scipy) >= 1.15
Requires:       python3dist(zarr) >= 3.0
Provides:       python3dist(xarray[io]) = %{version}-%{release}

%description -n python3-xarray+io
Metapackage for python3-xarray io extras.

%package -n       python3-xarray+etc
Summary:        Metapackage for python3-xarray etc extras
Requires:       python3-xarray = %{version}-%{release}
Requires:       python3dist(sparse) >= 0.15
Provides:       python3dist(xarray[etc]) = %{version}-%{release}

%description -n python3-xarray+etc
Metapackage for python3-xarray etc extras.

%package -n       python3-xarray+parallel
Summary:        Metapackage for python3-xarray parallel extras
Requires:       python3-xarray = %{version}-%{release}
Provides:       python3dist(xarray[parallel]) = %{version}-%{release}

%description -n python3-xarray+parallel
Metapackage for python3-xarray parallel extras.

%package -n       python3-xarray+viz
Summary:        Metapackage for python3-xarray viz extras
Requires:       python3-xarray = %{version}-%{release}
Requires:       python3dist(cartopy) >= 0.24
Requires:       python3dist(matplotlib) >= 3.10
Provides:       python3dist(xarray[viz]) = %{version}-%{release}

%description -n python3-xarray+viz
Metapackage for python3-xarray viz extras.

%package -n       python3-xarray+types
Summary:        Metapackage for python3-xarray types extras
Requires:       python3-xarray = %{version}-%{release}
Provides:       python3dist(xarray[types]) = %{version}-%{release}

%description -n python3-xarray+types
Metapackage for python3-xarray types extras.

%description

%package -n     python3-xarray
Summary:        N-D labeled arrays and datasets in Python
# oreon:reqs
Requires:       python3dist(numpy) >= 1.26
Requires:       python3dist(packaging) >= 24.2
Requires:       python3dist(pandas) >= 2.2
# /oreon:reqs
%description -n python3-xarray

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir xarray-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xarray usr/lib/python3*/site-packages/xarray* usr/lib64/python3*/site-packages/xarray* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xarray* usr/lib64/python3*/site-packages/xarray* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xarray -f %{oreon_filedir}/python3-xarray.list

%changelog

%autochangelog
