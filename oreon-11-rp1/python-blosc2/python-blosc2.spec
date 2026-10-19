%global source0_hash 4a867b0b177363ce43fea792b92723122966ff0ea99b5ab458268362cb1c411d
Name:           python-blosc2
Version:        4.13.1
Release:        1%{?dist}
Summary:        A fast _ compressed ndarray library with a flexible compute engine.
License:        BSD-3-Clause
URL:            https://github.com/Blosc/python-blosc2
Source0:        https://files.pythonhosted.org/packages/source/b/blosc2/blosc2-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3
BuildRequires:  python3dist(numpy) >= 2.1
BuildRequires:  python3dist(scikit-build-core) >= 0.11.0
Requires:       python3-blosc2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-blosc2+parquet
Summary:        Metapackage for python3-blosc2 parquet extras
Requires:       python3-blosc2 = %{version}-%{release}
Provides:       python3dist(blosc2[parquet]) = %{version}-%{release}

%description -n python3-blosc2+parquet
Metapackage for python3-blosc2 parquet extras.

%package -n       python3-blosc2+zarr
Summary:        Metapackage for python3-blosc2 zarr extras
Requires:       python3-blosc2 = %{version}-%{release}
Requires:       python3dist(zarr) >= 3.0.9
Provides:       python3dist(blosc2[zarr]) = %{version}-%{release}

%description -n python3-blosc2+zarr
Metapackage for python3-blosc2 zarr extras.

%package -n       python3-blosc2+hdf5
Summary:        Metapackage for python3-blosc2 hdf5 extras
Requires:       python3-blosc2 = %{version}-%{release}
Provides:       python3dist(blosc2[hdf5]) = %{version}-%{release}

%description -n python3-blosc2+hdf5
Metapackage for python3-blosc2 hdf5 extras.

%package -n       python3-blosc2+tui
Summary:        Metapackage for python3-blosc2 tui extras
Requires:       python3-blosc2 = %{version}-%{release}
Provides:       python3dist(blosc2[tui]) = %{version}-%{release}

%description -n python3-blosc2+tui
Metapackage for python3-blosc2 tui extras.

%package -n       python3-blosc2+hires
Summary:        Metapackage for python3-blosc2 hires extras
Requires:       python3-blosc2 = %{version}-%{release}
Provides:       python3dist(blosc2[hires]) = %{version}-%{release}

%description -n python3-blosc2+hires
Metapackage for python3-blosc2 hires extras.

%package -n       python3-blosc2+fsspec
Summary:        Metapackage for python3-blosc2 fsspec extras
Requires:       python3-blosc2 = %{version}-%{release}
Provides:       python3dist(blosc2[fsspec]) = %{version}-%{release}

%description -n python3-blosc2+fsspec
Metapackage for python3-blosc2 fsspec extras.

%description

%package -n     python3-blosc2
Summary:        A fast _ compressed ndarray library with a flexible compute engine.
# oreon:reqs
Requires:       python3dist(numexpr) >= 2.14.1
Requires:       python3dist(numpy) >= 1.26
# /oreon:reqs
%description -n python3-blosc2

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir blosc2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-blosc2 usr/lib/python3*/site-packages/blosc2* usr/lib64/python3*/site-packages/blosc2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/blosc2* usr/lib64/python3*/site-packages/blosc2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-blosc2 -f %{oreon_filedir}/python3-blosc2.list

%changelog

%autochangelog
