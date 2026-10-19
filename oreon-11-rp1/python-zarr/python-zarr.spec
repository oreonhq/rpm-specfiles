%global source0_hash b68676576a6fc42683dfcc0daeb3c0e994f71e1680696990bde056bd3acf3542
Name:           python-zarr
Version:        3.4.0
Release:        1%{?dist}
Summary:        An implementation of chunked, compressed, N-dimensional arrays for Python
License:        MIT
URL:            https://github.com/zarr-developers/zarr-python
Source0:        https://files.pythonhosted.org/packages/source/z/zarr/zarr-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.29.0
Requires:       python3-zarr = %{version}-%{release}
# /oreon:deps
%package -n       python3-zarr+remote
Summary:        Metapackage for python3-zarr remote extras
Requires:       python3-zarr = %{version}-%{release}
Requires:       python3dist(fsspec) >= 2023.10.0
Requires:       python3dist(obstore) >= 0.5.1
Provides:       python3dist(zarr[remote]) = %{version}-%{release}

%description -n python3-zarr+remote
Metapackage for python3-zarr remote extras.

%package -n       python3-zarr+gpu
Summary:        Metapackage for python3-zarr gpu extras
Requires:       python3-zarr = %{version}-%{release}
Provides:       python3dist(zarr[gpu]) = %{version}-%{release}

%description -n python3-zarr+gpu
Metapackage for python3-zarr gpu extras.

%package -n       python3-zarr+cast-value-rs
Summary:        Metapackage for python3-zarr cast-value-rs extras
Requires:       python3-zarr = %{version}-%{release}
Requires:       python3dist(cast-value-rs) >= 0.4.2
Provides:       python3dist(zarr[cast-value-rs]) = %{version}-%{release}

%description -n python3-zarr+cast-value-rs
Metapackage for python3-zarr cast-value-rs extras.

%package -n       python3-zarr+cli
Summary:        Metapackage for python3-zarr cli extras
Requires:       python3-zarr = %{version}-%{release}
Provides:       python3dist(zarr[cli]) = %{version}-%{release}

%description -n python3-zarr+cli
Metapackage for python3-zarr cli extras.

%package -n       python3-zarr+optional
Summary:        Metapackage for python3-zarr optional extras
Requires:       python3-zarr = %{version}-%{release}
Provides:       python3dist(zarr[optional]) = %{version}-%{release}

%description -n python3-zarr+optional
Metapackage for python3-zarr optional extras.

%description

%package -n     python3-zarr
Summary:        An implementation of chunked, compressed, N-dimensional arrays for Python
# oreon:reqs
Requires:       python3dist(donfig) >= 0.8
Requires:       python3dist(google-crc32c) >= 1.5
Requires:       python3dist(msgspec) >= 0.19
Requires:       python3dist(numcodecs) >= 0.14
Requires:       python3dist(numpy) >= 2
Requires:       python3dist(packaging) >= 22.0
Requires:       python3dist(typing-extensions) >= 4.14
# /oreon:reqs
%description -n python3-zarr

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zarr-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zarr usr/lib/python3*/site-packages/zarr* usr/lib64/python3*/site-packages/zarr* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zarr* usr/lib64/python3*/site-packages/zarr* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zarr -f %{oreon_filedir}/python3-zarr.list

%changelog

%autochangelog
