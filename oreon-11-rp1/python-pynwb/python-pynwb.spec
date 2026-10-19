%global source0_hash 681e86b73cf21fc607003936ac9e575efdb64d3d01001bfa351862d40f9b5e7e
Name:           python-pynwb
Version:        4.2.0
Release:        1%{?dist}
Summary:        Package for working with Neurodata stored in the NWB format.
License:        BSD-3-Clause
URL:            https://github.com/NeurodataWithoutBorders/pynwb
Source0:        https://files.pythonhosted.org/packages/source/p/pynwb/pynwb-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pynwb = %{version}-%{release}
# /oreon:deps
%package -n       python3-pynwb+zarr
Summary:        Metapackage for python3-pynwb zarr extras
Requires:       python3-pynwb = %{version}-%{release}
Requires:       python3dist(hdmf-zarr) >= 0.11.0
Requires:       python3dist(zarr) >= 2.12.0
Requires:       python3dist(zarr) < 3
Requires:       python3dist(numcodecs) >= 0.10.0
Requires:       python3dist(numcodecs) < 0.16.0
Provides:       python3dist(pynwb[zarr]) = %{version}-%{release}

%description -n python3-pynwb+zarr
Metapackage for python3-pynwb zarr extras.

%package -n       python3-pynwb+termset
Summary:        Metapackage for python3-pynwb termset extras
Requires:       python3-pynwb = %{version}-%{release}
Requires:       python3dist(linkml) >= 1.5.0
Requires:       python3dist(linkml-runtime) >= 1.5.5
Requires:       python3dist(schemasheets) >= 0.4.0
Requires:       python3dist(oaklib) >= 0.5.12
Provides:       python3dist(pynwb[termset]) = %{version}-%{release}

%description -n python3-pynwb+termset
Metapackage for python3-pynwb termset extras.

%description

%package -n     python3-pynwb
Summary:        Package for working with Neurodata stored in the NWB format.
# oreon:reqs
Requires:       python3dist(h5py) >= 3.6.0
Requires:       python3dist(hdmf) < 7
Requires:       python3dist(hdmf) >= 6.2.0
Requires:       python3dist(numpy) >= 1.24.0
Requires:       python3dist(pandas) >= 1.4.0
Requires:       python3dist(platformdirs) >= 4.2.2
Requires:       python3dist(python-dateutil) >= 2.8.2
# /oreon:reqs
%description -n python3-pynwb

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pynwb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pynwb usr/lib/python3*/site-packages/pynwb* usr/lib64/python3*/site-packages/pynwb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pynwb* usr/lib64/python3*/site-packages/pynwb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pynwb -f %{oreon_filedir}/python3-pynwb.list

%changelog

%autochangelog
