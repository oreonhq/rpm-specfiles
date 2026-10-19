%global source0_hash 69f48a60f62151d40c49fd6d9a6dc0b970aecef2813a33209e4dcde897fca48b
Name:           python-xarray-einstats
Version:        0.11.0
Release:        1%{?dist}
Summary:        Stats, linear algebra and einops for xarray
License:        ...
URL:            https://github.com/arviz-devs/xarray-einstats
Source0:        https://files.pythonhosted.org/packages/source/x/xarray_einstats/xarray_einstats-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.4
Requires:       python3-xarray-einstats = %{version}-%{release}
# /oreon:deps
%package -n       python3-xarray-einstats+einops
Summary:        Metapackage for python3-xarray-einstats einops extras
Requires:       python3-xarray-einstats = %{version}-%{release}
Provides:       python3dist(xarray-einstats[einops]) = %{version}-%{release}

%description -n python3-xarray-einstats+einops
Metapackage for python3-xarray-einstats einops extras.

%package -n       python3-xarray-einstats+numba
Summary:        Metapackage for python3-xarray-einstats numba extras
Requires:       python3-xarray-einstats = %{version}-%{release}
Requires:       python3dist(numba) >= 0.55
Provides:       python3dist(xarray-einstats[numba]) = %{version}-%{release}

%description -n python3-xarray-einstats+numba
Metapackage for python3-xarray-einstats numba extras.

%package -n       python3-xarray-einstats+test
Summary:        Metapackage for python3-xarray-einstats test extras
Requires:       python3-xarray-einstats = %{version}-%{release}
Requires:       python3dist(scipy) >= 1.15
Requires:       python3dist(preliz) >= 0.19
Provides:       python3dist(xarray-einstats[test]) = %{version}-%{release}

%description -n python3-xarray-einstats+test
Metapackage for python3-xarray-einstats test extras.

%package -n       python3-xarray-einstats+doc
Summary:        Metapackage for python3-xarray-einstats doc extras
Requires:       python3-xarray-einstats = %{version}-%{release}
Requires:       python3dist(sphinx) >= 5
Provides:       python3dist(xarray-einstats[doc]) = %{version}-%{release}

%description -n python3-xarray-einstats+doc
Metapackage for python3-xarray-einstats doc extras.

%description

%package -n     python3-xarray-einstats
Summary:        Stats, linear algebra and einops for xarray
# oreon:reqs
Requires:       python3dist(numpy) >= 2.0
Requires:       python3dist(scipy) >= 1.14
Requires:       python3dist(xarray) >= 2024.07.0
# /oreon:reqs
%description -n python3-xarray-einstats

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir xarray_einstats-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xarray-einstats usr/lib/python3*/site-packages/xarray_einstats* usr/lib64/python3*/site-packages/xarray_einstats* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xarray_einstats* usr/lib64/python3*/site-packages/xarray_einstats* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xarray-einstats -f %{oreon_filedir}/python3-xarray-einstats.list

%changelog

%autochangelog
